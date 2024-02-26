#
# Archivo: enteroPisoTecho.py
#
# Descripción: Archivo que permite obtener las funciones parte entera, piso y
#              techo.
#
# Fecha: 02/10/2017

class enteroPisoTecho():
    def __init__(self):
        pass

    def parteEntera(self,n):
        return int(n)

    def piso(self,n):
        if n >= 0:
            return int(n)
        else:
            return int(n)-1

    def techo(self,n):
        if self.n >= 0:
            return int(n)+1
        else:
            return int(n)

"""class enteroPisoTecho():
    def __init__(self,n):
        self.n = n

    def parteEntera(self):
        return int(self.n)

    def piso(self):
        if self.n >= 0:
            return int(self.n)
        else:
            return int(self.n)-1

    def techo(self):
        if self.n >= 0:
            return int(self.n)+1
        else:
            return int(self.n)"""
