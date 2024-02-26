import sys

################################################################################
#########  P E R M U T A C I O N E S   D E   U N   C O N J U N T O  ############
################################################################################

class permutaciones:

    final = []
    
    def hacerPermutacion(self,conj,mostrar):
        if conj == []:
            self.final.append(mostrar)
        else:
            for i in range(len(conj)):
                # Agregamos un nuevo elemento a la lista que se va a mostrar
                mostrarProv = mostrar[:]
                mostrarProv.append(conj[i])
                # Removemos el elemento recién agregado a "mostrar", del conjunto de 
                # sobrantes.
                conjProv = conj[:]
                conjProv.remove(conj[i])
                # Recursión, donde conj = conjProv, y mostrar = mostrarProv.
                self.hacerPermutacion(conjProv, mostrarProv)

    def funcion(self,conj):
        self.final = [] # Por si acaso se había hecho antes una permutación
        self.hacerPermutacion(conj,[])
        return self.final

"""
Nota: No sirve colocar el self.final = [] después del return,
      puesto que una vez hecho un return el programa no sigue
      leyendo lo que viene después.
"""

# Creamos el objeto permutaciones
permutaciones = permutaciones() 

################################################################################
#########################  P E D I R   D A T O S  ##############################
################################################################################

class pedirDatos:

    def numeroElementos(self,elemento,objeto):
        while True:
            try:
                N = int(input("Ingrese el número de "+str(elemento)+"s "+str(objeto)))
                assert(N >= 0)
                break
            except:
                print(">>> Debe ingresar un entero mayor o igual a cero")
                print(">>> Vuelva a intentarlo ")
                print("")
        return N
    
    def conjunto(self, articulo, elemento, tipoConjunto):    # Elemplos de artículos: "el ", "la ".
        sec = []
        N = self.numeroElementos(elemento, tipoConjunto)     # Ejemplos de tipoConjunto: "del conjunto: ", "del alfabeto: ", etc.
        print("")                                            # Ejemplos de elemento: "elemento", "letra", "fila", etc.
        for i in range(N):
            while True:
                try:
                    elem = input("Ingrese "+str(articulo)+str(elemento)+" "+str(i+1)+" "+str(tipoConjunto))
                    assert(elem not in sec)
                    sec.append(elem)
                    break
                except:
                    print(">>> Un conjunto no puede tener elementos repetidos")
                    print(">>> Vuelva a intentarlo")
                    print("")
        print("")
        return sec

# Creamos el objeto pedirDatos
pedirDatos = pedirDatos()

################################################################################
############################  I M P R I M I R  #################################
################################################################################

class imprimir:    
    def listaNumerada(self, conjunto):
        for i in range(len(conjunto)):
            print(str(i+1)+"- "+str(conjunto[i]))
        
# Creamos el objeto imprimir
imprimir = imprimir()

################################################################################
###########################  F A C T O R I A L  ################################
################################################################################

class factorial:   
    def funcion(self, x):
        if x == 0:
            n = 1
        else:
            n = x*self.funcion(x-1)
        return n

# Creamos el objeto factorial
factorial = factorial()

################################################################################
##########################  C O M B I N A T O R I O  ###########################
################################################################################

class combinatorio:
    def funcion(self,x,y):
        return factorial.funcion(x)/(factorial.funcion(y)*factorial.funcion(x-y))

# Creamos el objeto combinatorio
combinatorio = combinatorio()

################################################################################
############  P A R T I C I O N E S   D E   U N   C O N J U N T O  #############
################################################################################

class particiones:

    final = []
    cantidad = 0
    tamaños = [0,0,0,0,0,0,0,0,0,0,0,0]

    def hacerParticion(self,conj,mostrar):
        if conj == []:
            n = len(mostrar)
            self.tamaños[n-1] += 1
            self.cantidad += 1
        else:
            elem = conj[0]
            conj.remove(elem)
            conj2 = conj[:]
            i = 0
            while True:
                conj = conj2[:]
                auxMostrar = [k[:] for k in mostrar] 
                if i == len(mostrar):
                    if [] not in mostrar:
                        auxMostrar.append([elem])
                        self.hacerParticion(conj,auxMostrar)
                    break  
                else:
                    auxMostrar[i].append(elem)
                    self.hacerParticion(conj,auxMostrar)
                i += 1                   
    
    def funcion(self, conj):
        self.final = [] # Por si acaso se había hecho antes una partición
        self.cantidad = 0
        self.hacerParticion(conj,[[]])
        print(sum(self.tamaños)==self.cantidad)
        return self.tamaños, self.cantidad
# Creamos el objeto particiones
particiones = particiones()
                            
################################################################################
################  C O N V E R S I O N E S   D E   N Ú M E R O S  ###############
################################################################################

class conversion:

    def verificacion_numero_binario(self,cadena):
        try:
            assert(all(cadena[i] == "0" or cadena[i] == "1" for i in range(0,len(cadena))))
        except:
            print(">>> Esto no es un número binario ")
            sys.exit()
        
        
    def complementoDos_decimal(self,numero):
        cadena = str(numero)
        self.verificacion_numero_binario(cadena)
        primer_digito = int(cadena[0])
        res = (-1)*primer_digito * 2**(len(cadena)-1)
        print(res)
        for i in range(1, len(cadena)):
            digito = int(cadena[i])
            res += digito*10**(len(cadena)-1-i)
            print(res)
        return res

# Creamos el objeto conversion
conversion = conversion()
        
        
        



        
