#!/usr/bin/env python3
"""Gera os decks .odp do bootcamp a partir de um roteiro JSON, clonando as 4 paginas
do template oficial (capa, conteudo, secao, encerramento) para manter fundos, fontes e posicoes.

Uso: python3 tools/slides/gerar_slides.py aulas/aula-01-devops-overview/slides/aula-01.json [saida.odp]
Sem dependencias externas (so biblioteca padrao).
"""
import json, re, sys, zipfile, math, html
from pathlib import Path
from xml.sax.saxutils import escape

HERE = Path(__file__).resolve().parent
TEMPLATE = HERE / "template.odp"

# ---------- estilos extras (acrescentados aos automatic-styles do template) ----------
def tstyle(name, font, size, color, bold=False):
    w = "bold" if bold else "normal"
    return (f'<style:style style:name="{name}" style:family="text"><style:text-properties fo:color="{color}" '
            f'style:font-name="{font}" fo:font-size="{size}pt" fo:font-weight="{w}" style:font-name-asian="{font}" '
            f'style:font-size-asian="{size}pt" style:font-weight-asian="{w}" style:font-name-complex="{font}" '
            f'style:font-size-complex="{size}pt" style:font-weight-complex="{w}"/></style:style>')

EXTRA_STYLES = "".join([
    tstyle("TB", "Poppins", 14, "#000000"),                 # corpo 14pt
    tstyle("TBb", "Poppins", 14, "#000000", bold=True),     # corpo negrito
    tstyle("TBm", "Liberation Mono", 13, "#00048d"),        # inline code
    tstyle("TBh", "Poppins", 14, "#00048d", bold=True),     # destaque
    tstyle("TBs", "Poppins", 11, "#555555"),                # rodape
    tstyle("TCode", "Liberation Mono", 12, "#1a1a1a"),      # bloco de codigo
    tstyle("TCode11", "Liberation Mono", 11, "#1a1a1a"),    # bloco de codigo (linhas longas)
    tstyle("TCode10", "Liberation Mono", 10, "#1a1a1a"),    # bloco de codigo (linhas muito longas)
    tstyle("TT4b", "Poppins Medium", 28, "#00048d"),        # titulo longo
    tstyle("TT4c", "Poppins Medium", 24, "#00048d"),        # titulo muito longo
    tstyle("TT2b", "Poppins Medium", 56, "#00048d"),        # capa linha 1 longa
    tstyle("TT3b", "Poppins Light", 40, "#00048d"),         # capa linha 2 longa
    tstyle("TT8b", "Poppins Medium", 48, "#ffffff"),        # secao linha 1 longa
    tstyle("TT9b", "Poppins Light", 36, "#ffffff"),         # secao linha 2 longa
    '<style:style style:name="PBody" style:family="paragraph"><style:paragraph-properties fo:margin-top="0cm" fo:margin-bottom="0.15cm" fo:line-height="115%" fo:text-align="start"/></style:style>',
    '<style:style style:name="PCode" style:family="paragraph"><style:paragraph-properties fo:margin-top="0cm" fo:margin-bottom="0cm" fo:line-height="120%" fo:text-align="start"/></style:style>',
    # estilo de texto da caixa de codigo: a exportacao do Google Slides guarda o preenchimento da forma tambem aqui (como P5 no circulo verde)
    '<style:style style:name="PCodeBox" style:family="paragraph"><style:graphic-properties draw:fill="solid" draw:fill-color="#f1f3f4"/><style:paragraph-properties fo:text-align="start" style:font-independent-line-spacing="true"/><style:text-properties fo:font-size="12pt"/></style:style>',
    '<style:style style:name="grCode" style:family="graphic" style:parent-style-name="standard"><style:graphic-properties draw:stroke="none" svg:stroke-width="0cm" draw:fill="solid" draw:fill-color="#f1f3f4" draw:textarea-vertical-align="top" draw:auto-grow-height="true" fo:min-height="0cm" fo:padding-top="0.3cm" fo:padding-bottom="0.3cm" fo:padding-left="0.4cm" fo:padding-right="0.4cm" fo:wrap-option="wrap"/></style:style>',
])

CODE_GEOM = ('<draw:enhanced-geometry svg:viewBox="0 0 21600 21600" draw:type="rectangle" '
             'draw:enhanced-path="M 0 0 L 21600 0 21600 21600 0 21600 0 0 Z N"/>')
RECT_GEOM = ('<draw:enhanced-geometry draw:mirror-horizontal="false" draw:mirror-vertical="false" draw:text-areas="0 0 ?f3 ?f2" '
             'svg:viewBox="0 0 0 0" draw:type="ooxml-rect" draw:enhanced-path="M 0 0 L ?f3 0 ?f3 ?f2 0 ?f2 Z N">'
             '<draw:equation draw:name="f0" draw:formula="logwidth/2"/><draw:equation draw:name="f1" draw:formula="logheight/2"/>'
             '<draw:equation draw:name="f2" draw:formula="logheight"/><draw:equation draw:name="f3" draw:formula="logwidth"/></draw:enhanced-geometry>')

# ---------- texto ----------
def esc_text(s):
    """Escapa XML e preserva espacos multiplos/tabs (normaliza entidades HTML vindas do roteiro)."""
    s = html.unescape(s)
    out = []
    for i, part in enumerate(re.split(r"( {2,}|\t)", s)):
        if i % 2 == 0:
            out.append(escape(part))
        elif part == "\t":
            out.append("<text:tab/>")
        else:
            out.append(f'<text:s text:c="{len(part)}"/>')
    return "".join(out)

def inline(s, base="TB", bold="TBb", mono="TBm"):
    """Converte **negrito** e `codigo` em spans."""
    spans = []
    for tok in re.split(r"(\*\*[^*]+\*\*|`[^`]+`)", s):
        if not tok: continue
        if tok.startswith("**") and tok.endswith("**"):
            spans.append(f'<text:span text:style-name="{bold}">{esc_text(tok[2:-2])}</text:span>')
        elif tok.startswith("`") and tok.endswith("`"):
            spans.append(f'<text:span text:style-name="{mono}">{esc_text(tok[1:-1])}</text:span>')
        else:
            spans.append(f'<text:span text:style-name="{base}">{esc_text(tok)}</text:span>')
    return "".join(spans)

def para(s, pstyle="PBody", **kw):
    return f'<text:p text:style-name="{pstyle}">{inline(s, **kw)}</text:p>'

def shape(name, gstyle, x, y, w, h, body, tstyle="P2", geom=None):
    return (f'<draw:custom-shape draw:name="{name}" draw:style-name="{gstyle}" draw:text-style-name="{tstyle}" draw:layer="layout" '
            f'svg:width="{w:.3f}cm" svg:height="{h:.3f}cm" svg:x="{x:.3f}cm" svg:y="{y:.3f}cm">{body}{geom or RECT_GEOM}</draw:custom-shape>')

def est_lines(text, chars_per_line):
    return max(1, math.ceil(len(re.sub(r"\*\*|`", "", text)) / chars_per_line))

def notes_xml(n, texto):
    paras = "".join(f'<text:p text:style-name="P3"><text:span text:style-name="T5">{esc_text(l)}</text:span></text:p>'
                    for l in (texto or "").split("\n")) or "<text:p/>"
    return (f'<presentation:notes draw:style-name="dp2"><draw:page-thumbnail draw:name="thumb{n}" draw:style-name="gr2" draw:layer="layout" '
            f'svg:width="16.932cm" svg:height="9.524cm" svg:x="1.059cm" svg:y="1.905cm" draw:page-number="{n}" presentation:class="page"/>'
            f'<draw:frame draw:name="notes{n}" presentation:style-name="pr2" draw:text-style-name="P3" draw:layer="layout" svg:width="15.239cm" '
            f'svg:height="11.429cm" svg:x="1.905cm" svg:y="12.065cm" presentation:class="notes" presentation:placeholder="true" '
            f'presentation:user-transformed="true"><draw:text-box>{paras}</draw:text-box></draw:frame></presentation:notes>')

def page_open(n, dp):
    return (f'<draw:page draw:name="page{n}" draw:style-name="{dp}" draw:master-page-name="TITLE_5f_AND_5f_BODY" '
            f'presentation:presentation-page-layout-name="AL1T1">')

# ---------- tipos de slide ----------
def slide_capa(n, s):
    l1, l2 = s.get("titulo", ""), s.get("subtitulo", "")
    t2 = "T2" if len(l1) <= 10 else "TT2b"
    t3 = "T3" if len(l2) <= 16 else "TT3b"
    body = (f'<text:p text:style-name="P1"><text:span text:style-name="T1">. <text:s/></text:span></text:p>'
            f'<text:p text:style-name="P1"><text:span text:style-name="{t2}">{esc_text(l1)}</text:span></text:p>'
            f'<text:p text:style-name="P1"><text:span text:style-name="{t3}">{esc_text(l2)}</text:span></text:p>')
    return page_open(n, "dp1") + shape(f"s{n}a", "gr1", 1.59, 1.014, 18.183, 7.366, body) + notes_xml(n, s.get("notas")) + "</draw:page>"

def slide_secao(n, s):
    l1, l2 = s.get("titulo", ""), s.get("subtitulo", "")
    t8 = "T8" if len(l1) <= 12 else "TT8b"
    t9 = "T9" if len(l2) <= 16 else "TT9b"
    body = (f'<text:p text:style-name="P1"><text:span text:style-name="T7">. <text:s/></text:span></text:p>'
            f'<text:p text:style-name="P1"><text:span text:style-name="{t8}">{esc_text(l1)}</text:span></text:p>'
            f'<text:p text:style-name="P1"><text:span text:style-name="{t9}">{esc_text(l2)}</text:span></text:p>')
    return page_open(n, "dp4") + shape(f"s{n}a", "gr1", 3.169, 3.504, 18.108, 10.118, body) + notes_xml(n, s.get("notas")) + "</draw:page>"

def slide_encerramento(n, s):
    return page_open(n, "dp5") + notes_xml(n, s.get("notas")) + "</draw:page>"

def slide_conteudo(n, s):
    titulo = s.get("titulo", "")
    if len(titulo) <= 24:   t4, cpl, lh = "T4",   24, 1.45   # 34pt
    elif len(titulo) <= 34: t4, cpl, lh = "TT4b", 30, 1.20   # 28pt
    else:                   t4, cpl, lh = "TT4c", 36, 1.05   # 24pt
    title_lines = est_lines(titulo, cpl)
    title = f'<text:p text:style-name="P1"><text:span text:style-name="{t4}">{esc_text(titulo)}</text:span></text:p>'
    parts = [shape(f"s{n}t", "gr3", 2.323, 2.171, 18.452, 3.134, title)]
    # circulo verde decorativo do template
    parts.append(f'<draw:custom-shape draw:name="s{n}c" draw:style-name="gr4" draw:text-style-name="P5" draw:layer="layout" svg:width="2.137cm" svg:height="2.137cm" svg:x="-0.874cm" svg:y="2.208cm"><text:p/>'
                 '<draw:enhanced-geometry svg:viewBox="0 0 21600 21600" draw:type="ellipse" draw:enhanced-path="U 10800 10800 10800 10800 0 360 Z N"/></draw:custom-shape>')
    y = max(4.104, 2.171 + 0.25 + title_lines * lh + 0.35); CPL = 66; LH = 0.57
    body = []; lines = 0
    for p in s.get("paragrafos", []) or []:
        body.append(para(p)); lines += est_lines(p, CPL) + 0.3
    bl = s.get("bullets", []) or []
    if bl:
        items = "".join(f'<text:list-item>{para(b)}</text:list-item>' for b in bl)
        body.append(f'<text:list text:style-name="L2">{items}</text:list>')
        lines += sum(est_lines(b, CPL - 4) + 0.25 for b in bl)
    if s.get("destaque"):
        body.append(para(s["destaque"], base="TBh", bold="TBh")); lines += est_lines(s["destaque"], CPL) + 0.3
    if body:
        h = lines * LH + 0.6
        parts.append(shape(f"s{n}b", "gr1", 2.085, y, 18.452, h, "".join(body)))
        y += h + 0.15
    if s.get("codigo"):
        code_lines = s["codigo"].rstrip("\n").split("\n")
        longest = max(len(l) for l in code_lines)
        # escolhe a maior fonte que (a) nao quebra comandos literais longos e (b) cabe no espaco que sobra
        disponivel = 12.9 - y - (1.0 if s.get("rodape") else 0.0)
        opcoes = [("TCode", 69, 0.60), ("TCode11", 76, 0.55), ("TCode10", 84, 0.50)]
        if longest > 69: opcoes = opcoes[1:]
        if longest > 76: opcoes = opcoes[1:]
        for cstyle, cpl, clh in opcoes:
            wrapped = sum(max(1, math.ceil(len(l) / cpl)) for l in code_lines)
            h = wrapped * clh + 0.7
            if h <= disponivel: break
        code = "".join(f'<text:p text:style-name="PCode"><text:span text:style-name="{cstyle}">{esc_text(l) or "<text:s/>"}</text:span></text:p>' for l in code_lines)
        parts.append(shape(f"s{n}k", "grCode", 2.085, y, 18.452, h, code, tstyle="PCodeBox", geom=CODE_GEOM))
        y += h + 0.2
    if s.get("rodape"):
        parts.append(shape(f"s{n}r", "gr1", 2.085, y, 18.452, 1.0, para(s["rodape"], base="TBs", bold="TBs", mono="TBm")))
        y += 1.0
    aviso = ""
    if y > 13.1:
        aviso = f"  [AVISO] slide {n} ({titulo[:40]!r}) estoura a area util: y final ~{y:.1f}cm"
    return page_open(n, "dp3") + "".join(parts) + notes_xml(n, s.get("notas")) + "</draw:page>", aviso

# ---------- montagem ----------
def build(deck):
    with zipfile.ZipFile(TEMPLATE) as z:
        content = z.read("content.xml").decode("utf-8")
    head = content[:content.index("<office:automatic-styles>")]
    auto = re.search(r"<office:automatic-styles>(.*?)</office:automatic-styles>", content, re.S).group(1)
    tail_start = content.index("</office:presentation>")
    tail = content[tail_start:]  # </office:presentation></office:body></office:document-content>
    pres_open = re.search(r"<office:presentation[^>]*>", content).group(0)
    # declaracoes de cabecalho (header-decl etc.) antes da primeira draw:page
    pres_inner = content[content.index(pres_open) + len(pres_open):content.index("<draw:page ")]
    pages, avisos = [], []
    for i, s in enumerate(deck["slides"], start=1):
        tipo = s.get("tipo", "conteudo")
        if tipo == "capa": pages.append(slide_capa(i, s))
        elif tipo == "secao": pages.append(slide_secao(i, s))
        elif tipo == "encerramento": pages.append(slide_encerramento(i, s))
        else:
            x, a = slide_conteudo(i, s); pages.append(x)
            if a: avisos.append(a)
    new = (head + "<office:automatic-styles>" + auto + EXTRA_STYLES + "</office:automatic-styles>"
           + "<office:body>" + pres_open + pres_inner + "".join(pages) + tail)
    return new, avisos

def write_odp(deck, out):
    new_content, avisos = build(deck)
    with zipfile.ZipFile(TEMPLATE) as zin, zipfile.ZipFile(out, "w") as zout:
        zout.writestr(zipfile.ZipInfo("mimetype"), zin.read("mimetype"), compress_type=zipfile.ZIP_STORED)
        for item in zin.infolist():
            if item.filename in ("mimetype", "content.xml", "Thumbnails/thumbnail.png"): continue
            zout.writestr(item, zin.read(item.filename), compress_type=zipfile.ZIP_DEFLATED)
        zout.writestr("content.xml", new_content.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
    return avisos

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(1)
    src = Path(sys.argv[1]); deck = json.loads(src.read_text(encoding="utf-8"))
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".odp")
    avisos = write_odp(deck, out)
    print(f"{out}: {len(deck['slides'])} slides")
    for a in avisos: print(a)
