#!/bin/bash
cd /root/zrodelko
git add .
git commit -m "🛡️ Automatyczny backup: $(date)"
git push origin main
