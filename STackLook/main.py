
from getv import getv
from tra import tra
import sys
import os
from uno import obtener
from dos import tres
import time
#Colores
c1 = "\033[1;33;40m" #Yellow
c2 = "\033[1;34;40m" #Azul
c3 = "\033[1;35;40m" #Purpura
c4 = "\033[1;36;40m" #Cyan
c5 = "\033[1;37;40m" #Gris
c6 = "\033[1;31;40m" #Rojo
c7 = "\033[1;30;40m" #Negro
c8 = "\033[1;32;40m" #Verde
c9 = "\033[0;1m"     #Blanco1
c10 = "\033[96;1m"    #Aqua
#Colores2
c11 = "\033[36m"
c12 = '\033[34m'
c13 = '\033[33m'
c14 = "\033[96m"
#Colores2°
am = "\033[1;33;40m" #Yellow
az = "\033[1;34;40m" #Azul
mo = "\033[1;35;40m" #Purpura
cy = "\033[1;36;40m" #Cyan
bl = "\033[1;37;40m" #Gris
ro = "\033[1;31;40m" #Rojo
ne = "\033[1;30;40m" #Negro
ve = "\033[1;32;40m" #Verde
wh = "\033[0;1m"     #Blanco1
aq = "\033[96;1m"    #Aqua
#Tipografias
a1 = "\033[2;0;45m" #Sub-Morado
e2 = "\033[2;0;44m" #Sub-Azul
i3 = "\033[2;0;42m" #Sub-Verde
o4 = "\033[2;0;43m" #Sub-Amarillo
#Funciones
def sutil(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(12. / 150)

def corrida(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(3. / 250)

def xuxa(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(2. / 120)

def saludo(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(3. / 100)

def medio(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(8. / 200)

def lento(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 200)

def proceso(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(15. / 150)
def a():
	print (" ")
w = 0
v = sys.argv
can = len(v)
for c in v:
    w += 1
    d = c == 'start'
    if d == True:
        print('Iniciando traductor morse')
        if __name__ == '__main__':
            corrida(ro+f"""           
▒█▀▀▀█ ▀▀█▀▀ █▀▀█ █▀▀ █░█ ▒█░░░ █▀▀█ █▀▀█ █░█ 
░▀▀▀▄▄ ░░█░░ █▄▄█ █░░ █▀▄ ▒█░░░ █░░█ █░░█ █▀▄ 
▒█▄▄▄█ ░░▀░░ ▀░░▀ ▀▀▀ ▀░▀ ▒█▄▄█ ▀▀▀▀ ▀▀▀▀ ▀░▀
     {am}(Usar help para enlistar comandos)
            """+bl)
            while True:

                respuesta = input("$T:")
                if respuesta == 'help':
                    a0 = open('help.txt')
                    print(am+a0.read()+bl)
                elif respuesta == 'clt':
                    os.system('clear')
                elif respuesta == 'morencode':
                    inicio = getv() #Funcion que se encarga de obtener palabra, devolviendo el valor
                    translate = tra() #Traduce la palabra a morse usando el diccionario establecido
                    translate.tras(getv.a()) #Se asigna los valores que se obtuvieron en la entrada para posteriormente traducirlos
                elif respuesta == 'mordecode':
                    uno = obtener() #Lo mismo que la otra ;v
                    dos = tres()
                    dos.cuatro(obtener.inpp())
                elif respuesta == 'exit':
                    sutil(ro+'Saliendo...'+bl)
                    sys.exit()         
    else:
        if can == 1 or w == 2:
           print('Agregue start para iniciar')
