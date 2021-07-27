#PAquetes
 
#Modulos
import random
import os, sys, time
from random import choice, randrange
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
import os
paquete = ['playsound','gtts','kivy','phonenumbers']
def sutil(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(12. / 150)
print("///Instalador///")
print(f"""
{am}=====================
{ve}A){az}Instalar paquetes =
{ve}B){az}Eliminar paquetes =
{ve}C){az}Salir             =
{am}=====================
""")
a = 'a'
b = 'b'
c = 'c'
x = input('\nLetra:')
if x == a or x == a.upper():
    for i in paquete:
        sutil(ve+"instalando paquetes..."+bl)
        os.system("pip install {0}".format(i))
    sutil(am+'Proceso finalizado'+bl)
elif x == b or x == b.upper():
    sutil(ro+"borrando paquetes..."+bl)
    for g in paquete:
        os.system('pip uninstall {0}'.format(g))
    sutil(am+'Proceso finalizado'+bl)
else:
    sutil(ro+'Saliendo...'+bl)
    sys.exit()
