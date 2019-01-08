from gtts import gTTS
import winsound

import os


tts = gTTS(text='Good morning', lang='en')
tts.save("good.mp3")
os.system("good.mp3")

