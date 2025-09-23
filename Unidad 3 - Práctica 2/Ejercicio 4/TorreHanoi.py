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
        # Copiar discos actuales
        torreActual = []
        for i in range(self.__tope + 1):
            torreActual.append(self.__items[i])
    
        # Convertir a string
        contenido = ""
        for disco in torreActual:
            contenido += f"{disco} "
    
        # Usar formato con ancho fijo para alinear los corchetes
        # "<" alinea a la izquierda, el ancho total es max_discos*2
        print(f"Torre {numTorre}: [ {contenido:<{max_discos*2}}]")
    
    def verificarVictoria(self, cantidad_discos):
        # Paso 1: copiar los elementos de la torre en una lista
        torreActual = []
        for i in range(self.__tope + 1):
            torreActual.append(self.__items[i])

        # Paso 2: construir la torre esperada (ej: [3,2,1] para 3 discos)
        torreEsperada = []
        for disco in range(cantidad_discos, 0, -1):
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

    while not gano:
        try:
            origen = int(input("\nIngrese desde qué torre quiere mover un disco: "))
            destino = int(input("\nIngrese la torre destino: "))

            if origen in [1, 2, 3] and destino in [1, 2, 3]:
                if origen != destino:
                    if origen == 1 and not pila1.vacia():
                        if destino == 2:
                            if pila2.vacia():
                                disco = pila1.suprimir()
                                pila2.insertar(disco)
                                cantMovimientos += 1

                            elif pila2.getTope():
                                disco = pila1.suprimir()
                                if disco < pila2.getTope():
                                    pila2.insertar(disco)
                                    cantMovimientos += 1

                                else:
                                    print("\nERROR - El disco que se quiere mover es mayor que el último disco en la torre destino")
                                    pila1.insertar(disco)
                                    cantMovimientos -= 1

                        elif destino == 3:
                            if pila3.vacia():
                                disco = pila1.suprimir()
                                pila3.insertar(disco)
                                cantMovimientos += 1

                            elif pila3.getTope():
                                disco = pila1.suprimir()
                                if disco < pila3.getTope():
                                    pila3.insertar(disco)
                                    cantMovimientos += 1

                                else:
                                    print("\nERROR - El disco que se quiere mover es mayor que el último disco en la torre destino")
                                    pila1.insertar(disco)
                                    cantMovimientos -= 1

                    elif origen == 2 and not pila2.vacia():
                        if destino == 1:
                            if pila1.vacia():
                                disco = pila2.suprimir()
                                pila1.insertar(disco)
                                cantMovimientos += 1

                            elif pila1.getTope():
                                disco = pila2.suprimir()
                                if disco < pila1.getTope():
                                    pila1.insertar(disco)
                                    cantMovimientos += 1

                                else:
                                    print("\nERROR - El disco que se quiere mover es mayor que el último disco en la torre destino")
                                    pila2.insertar(disco)
                                    cantMovimientos -= 1

                        elif destino == 3:
                            if pila3.vacia():
                                disco = pila2.suprimir()
                                pila3.insertar(disco)
                                cantMovimientos += 1

                            elif pila3.getTope():
                                disco = pila2.suprimir()
                                if disco < pila3.getTope():
                                    pila3.insertar(disco)
                                    cantMovimientos += 1

                                else:
                                    print("\nERROR - El disco que se quiere mover es mayor que el último disco en la torre destino")
                                    pila2.insertar(disco)
                                    cantMovimientos -= 1

                    elif origen == 3 and not pila3.vacia():
                        if destino == 1:
                            if pila1.vacia():
                                disco = pila3.suprimir()
                                pila1.insertar(disco)
                                cantMovimientos += 1

                            elif pila1.getTope():
                                disco = pila3.suprimir()
                                if disco < pila1.getTope():
                                    pila1.insertar(disco)
                                    cantMovimientos += 1

                                else:
                                    print("\nERROR - El disco que se quiere mover es mayor que el último disco en la torre destino")
                                    pila3.insertar(disco)
                                    cantMovimientos -= 1

                        elif destino == 2:
                            if pila2.vacia():
                                disco = pila3.suprimir()
                                pila2.insertar(disco)
                                cantMovimientos += 1

                            elif pila2.getTope():
                                disco = pila3.suprimir()
                                if disco < pila2.getTope():
                                    pila2.insertar(disco)
                                    cantMovimientos += 1

                                else:
                                    print("\nERROR - El disco que se quiere mover es mayor que el último disco en la torre destino")
                                    pila3.insertar(disco)
                                    cantMovimientos -= 1

            else:
                print("\nERROR - Torre/s no válida/s")

        except:
            TypeError("ERROR - Se esperaba un número")
        
        mostrarTorres(pila1, pila2, pila3, n)
        gano = pila3.verificarVictoria(n)

    print()
    print("¡Felicidades, ganaste el juego!".center(60))
    print(f"Cantidad de movimientos realizados: {cantMovimientos}\nNúmero mínimo de movimientos para ganar: {(2**n) - 1}\n")

        
