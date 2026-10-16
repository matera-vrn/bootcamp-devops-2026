#!/bin/bash
set -e
echo "===== PIPELINE INICIADA - $(date '+%H:%M:%S') ====="
./build.sh
./test.sh
./deploy.sh
echo "===== PIPELINE VERDE - aplicacao em producao! ====="
