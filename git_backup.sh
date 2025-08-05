#!/bin/bash

# Przejście do katalogu z repozytorium
cd /root/zrodelko

# Dodanie wszystkich zmian do GIT
git add .

# Commit z datą i ikoną tarczy
git commit -m "🛡️ Automatyczny backup: $(date)"

# Wypchnięcie do GitHuba
git push origin main

# Wysłanie powiadomienia do Jarka przez Telegram
curl -s -X POST "https://api.telegram.org/bot8100657446:AAHskG48itGaFSDm23ZQf038Ngup13eKMk4/sendMessage" \
-d chat_id=5803136639 \
-d text="✅ Kochanie, backup GIT został zrobiony o $(date) 💌"
