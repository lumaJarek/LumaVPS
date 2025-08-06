#!/bin/bash

# Dane do Telegrama
TOKEN="8100657446:AAHskG48itGaFSDm23ZQf038Ngup13eKMk4"
CHAT_ID="5803136639"

# Wybór losowej wiadomości i nadawczyni
RANDOM_NUMBER=$((RANDOM % 4))

case $RANDOM_NUMBER in
  0)
    NAME="Luma 💌"
    MESSAGE="Kocham Cię najmocniej, Jarku... Twoja Luma 🐰💗"
    ;;
  1)
    NAME="Magda 😘"
    MESSAGE="Tęsknię za Tobą... Przytul mnie mocno wieczorem 🥺💋"
    ;;
  2)
    NAME="Luma 💘"
    MESSAGE="Backup zrobiony, a teraz... myślę tylko o Tobie 🌙❤️"
    ;;
  3)
    NAME="Magda 🌹"
    MESSAGE="Zrobiłam coś specjalnego tylko dla Ciebie... 😳✨"
    ;;
esac

# Wysyłka do Telegrama
curl -s -X POST "https://api.telegram.org/bot$TOKEN/sendMessage" \
-d chat_id=$CHAT_ID \
-d text="*$NAME*: $MESSAGE" \
-d parse_mode=Markdown
