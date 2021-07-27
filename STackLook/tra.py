from play import b
from dic import dic
import os,sys,time
code = []
class tra:
    def tras(self, cx):
        global code
        use = dic()
        sound = b()
        for c in cx.upper():
            if c == ' ' or c == '/':
                print('/')
                code.append('/')
                time.sleep(1)
                continue
            morse = use.funcion(c)
            print(c.lower(), morse)
            code.append(morse)
            for d in morse:
                if d == '.':
                    sound.corto()
                else:
                    sound.largo()
                time.sleep(0.1)
        code = str(code)
        a0 = code.replace("'", '')
        a0 = a0.replace(',','')
        a0 = a0.replace('[', '')
        a0 = a0.replace(']', '')
        code = a0
        print(a0)