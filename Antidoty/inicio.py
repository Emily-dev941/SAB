import os,sys,time
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

def sup(d):
    for c in d+'\n':
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(6./100)
dic = open('datebase.txt')
dic = dic.read()
base = dic.split()
u=sys.argv
negativo = 'n'
positivo = 'y'
def escaneo(db, archivo):
    ran = 0
    for r in db:
        prueba=archivo.find(r)
        if prueba >= 0:
            ran = ran + 1 
            sup(f'{ro}Existe la palabra "{r}" en el archivo...'+bl)
        else:
            print(ve+f'Palabra {r} inexistente'+bl)
    sup(f'\n{bl}Se han encontrado {am}{ran} {bl}palabras sospechosas en el codigo')
    print("¿Ejecutar? Y/N/  X = Mostrar codigo")
    respuesta = input('>>>')
    print()
    if respuesta == negativo or respuesta == negativo.upper():
        sup('{0}({2}*{1}){3}El programa no se ejecutará'.format(bl,bl,az,az))
        sys.exit()
    elif respuesta == positivo or respuesta == positivo.upper():
        sup('{0}({2}*{1}){3}Ejecutando'.format(bl,bl,az,az))
        time.sleep(1)
        os.system('python '+ ruta+'/'+File)
    elif respuesta == 'x' or respuesta == 'X':
        sup("{0}({2}*{1}){3}Codigo:".format(bl,bl,az,az))
        print(archivo)

try:
   ruta = u[-2]
   File = u[-1]
except IndexError:
    sup('{2}Por favor use la siguiente {0}sintaxis{1} al ejecutar el programa{3}:'.format(am,az,az,am))
    print('python inicio.py "ruta" "archivo"')
try:
   x=os.path.isdir(ruta)
   y=os.path.isfile(File)
   if x == False:
       sup(ro+'La ruta que estableciste no se existe!'+bl)
   elif x == True and y == True:
       z0=open(File, 'r')
       objetivo = z0.read()
       escaneo(base,objetivo)
except NameError:
    print(f'{bl}[{ro}ERROR{bl}] {am}Ruta no definida{bl}')