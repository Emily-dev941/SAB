import os,sys,time 
#FUNCIONES
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
ver = []
os.system("cls")
os.system("color 0b")
sutil("Distribuidor python para windows")
user = input("Username:")
yes = 'Y'
no = 'N'
def cuerpo():
   os.system('md output')
   print ("Que version de python usas?")
   try:
      c = int(input("Python"))
      ver.append(c)
   except ValueError: 
      sutil("Escribe con numeros enteros ejemplo:..37,38,39")
      ver.clear()
      cuerpo()
   os.system(f'COPY C:\\Users\\{user}\AppData\\Roaming\\Python\\Python{ver[0]}\\Scripts\\pyinstaller.exe C:\\Users\\{user}\\Desktop\\distribuidor\\output')
   ruta=input("Agrega el archivo (INCLUYENDO RUTA)\n>>>")
   os.system(f'COPY {ruta} C:\\Users\\{user}\\Desktop\\distribuidor\\output ')
   operacion_normal =f'cd C:\\Users\\{user}\\Desktop\\distribuidor\\output && pyinstaller {ruta}'
   ocultar_consola =f'cd C:\Program Files\Python{ver[0]}\Scripts && pyinstalsler --windowed {ruta}' 
   operaciones = {
   '1':operacion_normal}
   def menu():
      print("""
1) Compresion (Predeterminada)
2) Compresion (Personalizada)
3) Salir...
      """)
      try:
         
         r1 = int(input("Opcion:"))
         if r1 == 1:
            os.system(operaciones["1"])
            time.sleep(11)
            os.system("cls")
            sutil("Proceso terminado.")
            time.sleep(2)
            exit()
         elif r1 == 2:
            parametro = []
            c1 = input("Comprimir en un solo archivo y/n\n>>>")
            if c1 == no or c1 == no.lower():
               parametro.append("")
            elif c1 == yes or c1 == yes.lower():
               parametro.append(" --onefile ")
            else:
               os.system('cls')
               time.sleep()
               menu()
            c2 = input("Ocultar Consola de comandos y/n\n>>>")
            if c2 == no or c2 == no.lower():
               parametro.append("")
            elif c2 == yes or c2 == yes.lower():
               parametro.append(" --windowed ")
            else:
               os.system('cls')
               time.sleep()
               menu()
            c3 = input("Agregar icono y/n\n>>>")
            if c3 == no or c3 == no.lower():
               parametro.append("")
               parametro.append("")
            elif c3 == yes or c3 == yes.lower():
               parametro.append(" --icon=")
               c4 = input("Ruta\archivo.ico\n")
               c4 = c4+' '
               parametro.append(c4)
            else:
               os.system('cls')
               time.sleep()
               menu()
            operacion_personalizada =f'cd C:\\Users\\{user}\\Desktop\\distribuidor\\output && pyinstaller{parametro[0]}{parametro[1]}{parametro[2]}{parametro[3]}{ruta}' 
            os.system(operacion_personalizada)
            print(operacion_personalizada)
         elif r1 == 3:
            print("Vuelve pronto!!")
            sutil("saliendo...")
            time.sleep(3)
            exit()
         else:
            os.system('cls')
            corrida('Solo puedes responder con un numero del 1-3')
            time.sleep(4)
            os.system('cls')
            
      except ValueError:
         sutil("Responde con numeros enteros")
         menu()
   menu()
bucle0= True
while bucle0:
   print ("instalar paquetes y/n")
   r0 = input(">>>")
   if r0 == yes or r0 == yes.lower():
      os.system('pip install -r requisitos')
      bucle0 = False
      cuerpo()
   elif r0 == 'help':
      u = open('help')
      u = u.read()
      os.system('cls')
      time.sleep(3)
      corrida(u)
      os.system("pause")
      time.sleep(2)
      os.system('cls')
      bucle0 = True
   elif r0 == no or r0 == no.lower():
      os.system('cls')
      bucle0=False
      cuerpo()
   else:
      sutil("Responde Y o S")
      bucle0 = True
      