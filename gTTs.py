from gtts import gTTS
#gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with,
# Google Translate's text-to-speech API

import os

#you have to write your text in mytext variable
mytext = 'My Name is John'
# you can select your language code if english--> en ,
language = 'en'


myobj = gTTS(text=mytext, lang=language, slow=False)


myobj.save("welcome.mp3")

os.system("welcome.mp3")
