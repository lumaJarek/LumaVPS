import os
import sys
from edge_tts import Communicate
import asyncio

async def main():
    text = " ".join(sys.argv[1:])
    communicate = Communicate(text, voice="en-US-JennyNeural")
    await communicate.save("luma_mowi.mp3")
    os.system("ffplay -nodisp -autoexit luma_mowi.mp3")

asyncio.run(main())
