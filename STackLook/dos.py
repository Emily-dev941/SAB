import re
from cid import bv0
import time
from repro import reproductor
class tres():
    def cuatro(self, valor):
        code = []
        valor = valor.split()
        use = bv0()
        rep = reproductor()
        for c in valor:
            if c == ' ' or c == '/':
                print('/')
                code.append('/')
                time.sleep(1)
                continue
            morse = use.funcion(c)
            print(c.lower(), morse)
            code.append(morse)
        a1 = str(code)
        a0 = a1.replace("'", '')
        a0 = a0.replace(',','')
        a0 = a0.replace('[', '')
        a0 = a0.replace(']', '')
        a0 = a0.replace(' ', '')
        a0 = a0.replace('/', ' ')
        print(a0)
        rep.crear(a0)
        rep.reproducir()



