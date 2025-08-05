from gtts import gTTS
import sys
import os

text = " ".join(sys.argv[1:])
tts = gTTS(text=text, lang='pl')
tts.save("luma_mowi_pl.mp3")

# Odtwórz tylko jeśli karta dźwiękowa działa:
# os.system("mpg123 luma_mowi_pl.mp3")
