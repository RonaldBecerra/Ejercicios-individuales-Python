#
# Archivo: particiones.py
#
# Descripción: Ésta es la mejor forma que se me ha ocurrido para generar las particiones
#              Genera las particiones con un solo elemento; luego, por cada partición
#              creada, va anexando un elemento adicional en los subconjuntos
#
# Fecha: 21/07/2019
#

def particiones(conjunto):
    if conjunto == []:
        return []
        
    else:
        particiones = []
        particiones.append([[conjunto[0]]])
        lista = conjunto[1:]
        
        while lista != []:
            nuevoElem = lista[0]
            lista.remove(nuevoElem)
            particionesAux = []
            
            for p in particiones:
                # Caso en que el nuevo elemento se agrega en un conjunto aislado
                nuevaParticion = []
                for sublista in p:
                    nuevaParticion.append(sublista[:])
                nuevaParticion.append([nuevoElem])
                particionesAux.append(nuevaParticion)
                
                contador = 0
                maximo = len(p)
                while contador < maximo:
                    nuevaParticion = []
                    for sublista in p:
                        nuevaParticion.append(sublista[:])
                    nuevaParticion[contador].append(nuevoElem)
                    particionesAux.append(nuevaParticion)
                    contador += 1

            particiones = particionesAux[:]

        return particiones
                
                
                
                
                        
                
        
