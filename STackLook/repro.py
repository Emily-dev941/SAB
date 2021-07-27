#reproductor de audio
import os
from playsound import playsound
from gtts import gTTS
from random import randint
class reproductor:
    global lenguaje
    lenguaje = 'es'
    def crear(self, texto):
        r1 = randint(0,99999999999999)
        l1 = randint(0,99999999999999)
        global filename
        filename = str(r1)+'archivo'+str(l1)+'.mp3'
        tipo = gTTS(lang=lenguaje,text=str(texto), slow=False)
        tipo.save(filename)
    def reproducir():
        playsound(filename, True)
        os.remove(filename)
        
