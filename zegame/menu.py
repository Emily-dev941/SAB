from tkinter import *
import os, sys, time
import webbrowser
from random import choice
window = Tk()
window.title('Menu Principal')
window.geometry('900x500')
window.config(background='grey4')
zeroprofile = 'https://t.me/RedNull000'
#Funciones
def cierre():
    time.sleep(0.2)
    window.destroy()
    exit()
def reinicio():
    time.sleep(0.5)
    window.destroy()
    os.system('python menu.py')
    exit()

def contactanos(x):
    time.sleep(0.2)
    if x == 0:
        webbrowser.open(youtube, new=1, autoraise=True)
        x = x + 1 
    if x == 1:
        webbrowser.open(discord, new=1, autoraise=True)
        x = x + 1
    if x == 2:
        webbrowser.open(whatsapp, new=1, autoraise=True)
        x = x + 1
    if x == 3:
        webbrowser.open(telegram, new=1, autoraise=True)
        x = x + 1 
def underzero():
    time.sleep(0.2)
    webbrowser.open(zeroprofile, new=1, autoraise=True)
def configure():
    time.sleep(0.2)
    cm = Tk()
    cm.title('Configuracion')
    cm.config(background='grey5')
    cm.geometry('300x300')
    while True:
        cm.update()
        col = choice(['red','yellow','blue','green'])
        text3 = Text(cm, background=None, foreground=col, width=10000, height=-3, font=("Verdana",24))
        text3.config(state= None)
        text3.pack(anchor=CENTER)
        txt3 = 'Proximamente!'
        text3.insert(INSERT,txt3)
        time.sleep(0.1)
def juego():
    os.system('python demo.py')
    time.sleep(0)

color_0 = 'dark slate gray' #Fondo
color_1 = 'slate gray' #Texto
alto, ancho = -2,7
youtube = 'https://www.youtube.com/channel/UC7cxeveiSyiKSNYadWWUhEg' #0
discord = 'https://discord.gg/YZFzJGFcep' #1 
whatsapp = 'https://chat.whatsapp.com/FBfPUbijXMwEQJc2CYUigI' #2 
telegram = 'https://t.me/VTA_DB' #3
#Contactanos
contact = Button(window, text='VTA', bg=color_0, fg=color_1, width=10, height=alto, font=('Comic Sans MS', 24), command=lambda:contactanos(0)).grid(row=4, column=3, pady=0)#Vta
zero = Button(window, text='UnderZero', bg=color_0, fg=color_1, width=10, height=alto, font=('Comic Sans MS', 24), command=lambda:underzero()).grid(row=4, column=1, pady=0)
#Menu
end = Button(window, text="Salir" ,bg=color_0, fg=color_1, width=9 ,height=alto, font=("Verdana",24),command=lambda:cierre()).grid(row=3,column=2,pady=50, padx=0.01) #cerrar
restart = Button(window, text="Reiniciar",bg=color_0,fg=color_1, width=10, height=alto, font=('Verdana',24), command=lambda:reinicio()).grid(row=3, column=3, pady=0.01, padx=0.01) #Reiniciar
config = Button(window, text='Configurar', bg=color_0, fg=color_1, width=10, height=alto, font=('Verdana',24), command=lambda:configure()).grid(row=3, column=1, pady=0.01, padx=0.01)
#Play
end = Button(window, text="Play" ,bg=color_0, fg=color_1, width=10 ,height=alto, font=("Verdana",24),command=lambda:juego()).grid(row=1,column=2,pady=50, padx=0.01) #iniciar juego
while True:
   window.update()
   rain = choice(['red', 'pink', 'blue', 'white', 'yellow'])
   texto = Text(window, background=None, foreground=rain, width=10000, height=-3, font=("Verdana",24))
   texto.config(state= None)
   texto.grid(row=1, column=4, pady=0.01)
   txt = 'Play!'
   a0,a1,a2,a3,a4 = txt.upper(), txt.lower(), txt.capitalize(), txt.title(), txt.swapcase()
   a5 = choice([a0,a1,a2,a3,a4])
   time.sleep(0.1)
   texto.insert(INSERT,a5)
   
   text1 = Text(window, background=None, foreground=rain, width=10000, height=-3, font=("Verdana",24))
   text1.config(state= None)
   text1.grid(row=3, column=4, pady=0.01, padx=0.01)
   txt1 = 'Menu!'
   b0,b1,b2,b3,b4 = txt1.upper(), txt1.lower(), txt1.capitalize(), txt1.title(), txt1.swapcase()
   a5 = choice([b0,b1,b2,b3,b4])
   time.sleep(0.1)
   text1.insert(INSERT,a5)

   text2 = Text(window, background=None, foreground=rain, width=10000, height=-3, font=("Verdana",24))
   text2.config(state= None)
   text2.grid(row=4, column=4, pady=0.01)
   txt2 = 'Contactame!'
   c0,c1,c2,c3,c4 = txt2.upper(), txt2.lower(), txt2.capitalize(), txt2.title(), txt2.swapcase()
   a5 = choice([c0,c1,c2,c3,c4])
   time.sleep(0.1)
   text2.insert(INSERT,a5)