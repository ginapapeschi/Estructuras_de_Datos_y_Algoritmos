import numpy as np

class PilaSecuencial:
    __tope: int
    __max: int
    __cant: int
    __items: np.ndarray

    def __init__(self, max):
        self.__tope = -1
        self.__max = max
        self.__cant = 0
        self.__items = np.empty(max, dtype=int)

    def getTope(self):
        if self.vacia():
            return None
        else: return self.__items[self.__tope]

    def getCantidad(self):
        return self.__cant
    
    def llena(self):
        return self.__cant == self.__max
    
    def vacia(self):
        return self.__tope == -1
    
    def insertar(self, elemento):
        self.__tope += 1
        self.__items[self.__tope] = elemento
        self.__cant += 1
        #print(f"Elemento insertado en la posición {self.__tope}")

    def suprimir(self):
        if self.vacia():
            print("La pila está vacía")

        else:
            elemento = self.__items[self.__tope]
            self.__tope -= 1
            return elemento        
                
    def mostrar(self, numTorre, max_discos):
        # Copiar discos actuales en una lista para poder comparar fácilmente.
        torreActual = []
        for i in range(self.__tope + 1): # Recorre desde el disco inferior (0) hasta el superior (self.__tope).
            torreActual.append(self.__items[i]) # Tiene la secuencia de discos de abajo hacia arriba.
    
        # Convertir a string
        contenido = ""
        for disco in torreActual:
            contenido += f"{disco} " # Construye un string con todos los discos de la torre. Si torreActual = [3,2,1], contenido será "3 2 1 "
    
        # Usar formato con ancho fijo para alinear los corchetes
        # "<" alinea a la izquierda, el ancho total es max_discos*2
        print(f"Torre {numTorre}: [ {contenido:<{max_discos*2}}]") # Se asegura que el contenido se alinee a la izquierda y ocupe un ancho suficiente para mostrar todos los discos sin que se vea desordenado.
    
    def verificarVictoria(self, cantidad_discos):
        # Paso 1: copiar los elementos de la torre en una lista, igual que en mostrar.
        torreActual = []
        for i in range(self.__tope + 1):
            torreActual.append(self.__items[i])

        # Paso 2: construir la torre esperada (ej: [3,2,1] para 3 discos)
        torreEsperada = []
        for disco in range(cantidad_discos, 0, -1): # range(inicio, fin, paso)
            torreEsperada.append(disco)

        # Paso 3: comparar torre actual con la torre esperada
        if torreActual == torreEsperada:
            return True
        else:
            return False

def mostrarTorres(pila1, pila2, pila3, maxDiscos):
    print("\nTorres actuales:")
    pila1.mostrar(1, maxDiscos)
    pila2.mostrar(2, maxDiscos)
    pila3.mostrar(3, maxDiscos)

if __name__ == '__main__':
    print()
    print("¡Bienvenido al juego de Torres de Hanoi!".center(60))
    gano = False
    cantMovimientos = 0
    n = int(input("\nIngrese el número de discos: "))

    pila1 = PilaSecuencial(n)
    pila2 = PilaSecuencial(n)
    pila3 = PilaSecuencial(n)
    for i in range (n, 0, -1):
        pila1.insertar(i)

    print()
    print("¡Comenzó el juego!".center(60))
    mostrarTorres(pila1, pila2, pila3, n)

    torres = [pila1, pila2, pila3]

    while not gano:
        try:
            origen = int(input("\nIngrese desde qué torre quiere mover un disco: "))
            destino = int(input("\nIngrese la torre destino: "))
            if origen in [1, 2, 3] and destino in [1, 2, 3]:
                if origen != destino:
                    torreOrigen = torres[origen - 1] # Usa de índice la torre de origen ingresada para acceder a ella.
                    torreDestino = torres[destino - 1] # Lo mismo pero con la de destino.
                    
                    if torreOrigen.vacia(): # Reemplaza if origen == X and not pilaX.vacia()
                        print("\nERROR - La/s torre/s está/n vacía/s")

                    else:
                        disco = torreOrigen.suprimir() # Reemplaza el disco = pilaX.suprimir()
                        
                        if torreDestino.vacia() or disco < torreDestino.getTope():
                            torreDestino.insertar(disco)
                            cantMovimientos += 1
                        
                        else:
                            print("\nERROR - El disco que se quiere mover es mayor que el último disco en la torre destino")
                            torreOrigen.insertar(disco) # Vuelve a insertar el disco que quitó.
                            # No es necesario que cambie cantMovimientos, ya que se actualiza sólo cuando mueve un disco.
                
                else: # if origen == destino:
                    print("\nERROR - La torre destino es igual a la torre de origen")
            else: # if origen - 1 in [1, 2, 3] and destino - 1 in [1, 2, 3]:
                print("\nERROR - Torre/s no válida/s")

        except ValueError:
            print("ERROR - Se esperaba un número")
        
        mostrarTorres(pila1, pila2, pila3, n)
        gano = pila3.verificarVictoria(n)

    print()
    print("¡Felicidades, ganaste el juego!".center(60))
    print(f"Cantidad de movimientos realizados: {cantMovimientos}\nNúmero mínimo de movimientos para ganar: {(2**n) - 1}\n")