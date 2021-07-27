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
import os,sys,time, random
#Funciones
def xemp(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. /10000)
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
#valores predeterminados
longuitud = 3
veces = 5
cero = 0
caracteres = ['abcdario', 'numeros']
diultra = ['simple01']
dirandom = ['uno', 'dos']
diccionarios = 1
#personalizadowww
p = []
def ultra(diccionario):
    contenedor = []
    uso = open(diccionario)
    medio = uso.read()
    entero = medio.split()
    pultim = len(entero)
    for x in range(0,longuitud):
        a = random.choice(entero)
        contenedor.append(a)
    cv = ''
    for u in range(len(contenedor)):
       cv = cv + contenedor[u]
    print(cv)
    
def cartes(liston):
    contenedor = []
    uso = open(liston)
    medio = uso.read()
    entero = medio.split()
    for u in range(0, longuitud):
        a = random.choice(entero)
        contenedor.append(a)
    vc = ''
    for o in range(len(contenedor)):
        vc = vc + contenedor[o]
    print(vc)

def numos(umeros):
     contenedor = []
     uso = open(umeros)
     medio = uso.read()
     entero = medio.split()
     for c in range(0, longuitud):
         f = random.choice(entero)
         contenedor.append(f)
     void = ''
     for j in range(longuitud):
         void = void + contenedor[j]
     print(void)


print(f'''
{cy}-------------------------------------
{ve}-1) UltraRandom
{ve}-2) Caracteres
{ve}-3) Numeros
{ve}-4) Salir

{ro}x {bl}= valor predeterminado
{cy}-------------------------------------
''')
while True:
    respuesta = int(input('>>>'))
    if respuesta == 1:
        du = input(am+'Veces:'+ro)
        if du == 'x' or du == 'X':
            xd = None
        else:
            veces = int(du)
        di = input(am+'Longuitud:'+ro)
        if di == 'x' or di == 'X':
            xd = None
        else:
            longuitud = int(di)
        print(bl)
        for c in range(0,veces):
           ultra(diultra[0])

    elif respuesta == 2:
        du = input(am+'Veces:'+ro)
        if du == 'x' or du == 'X':
            xd = None
        else:
            veces = int(du)
        #Longuitud
        di = input(am+'Longuitud:'+ro)
        if di == 'x' or di == 'X':
            xd = None
        else:
            longuitud = int(di)
        print(bl)
        for c in range(0,veces):
           cartes(caracteres[0])
    elif respuesta == 3:
        du = input(am+'Veces:'+ro)
        if du == 'x' or du == 'X':
            xd = None
        else:
            veces = int(du)
        di = input(am+'Longuitud:'+ro)
        if di == 'x' or di == 'X':
            xd = None
        else:
            longuitud = int(di)
        print(bl)
        for c in range(0,veces):
           numos(caracteres[1])