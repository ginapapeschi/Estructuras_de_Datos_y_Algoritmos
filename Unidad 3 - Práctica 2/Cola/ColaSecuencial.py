import numpy as np

class ColaSecuencial:
    __primero: int # Índice del primer elemento de la cola.
    __ultimo: int  # Índice de la siguiente posición LIBRE donde se insertará un elemento.
    __max: int
    __cant: int
    __items: np.ndarray

    def __init__(self, max):
        self.__primero = 0
        self.__ultimo = 0
        self.__max = max
        self.__cant = 0
        self.__items = np.empty(max, dtype=int)

    def vacia(self):
        return self.__cant == 0
    
    def llena(self):
        return self.__cant == self.__max
    
    def getPrimero(self):
        return self.__primero
    
    def getUltimo(self):
        return self.__ultimo
    
    def insertar(self, elemento):
        if not self.llena():
            self.__items[self.__ultimo] = elemento
            self.__ultimo = (self.__ultimo + 1) % self.__max # Actualiza self.__ultimo de forma circular (si llega la final, vuelve al inicio).
            # (self.__ultimo + 1) avanza el índice al siguiente lugar en el arreglo.
            # % self.__max devuelve self.__ultimo al inicio (operación módulo o resto):
            # self.__ultimo + 1 = 5
            # 5 % 5 = 0 -> vuelve al inicio del arreglo.

            self.__cant += 1
            print(f"Elemento {elemento} insertado")
            return elemento
        
        else:
            print("Cola llena")
            #self.suprimir()
            #self.insertar(elemento)    # Si se quiere hacer inserción automática aunque esté lleno.

    def suprimir(self):
        if self.vacia():
            print("Cola vacía")

        else:
            elemento = self.__items[self.__primero]
            self.__primero = (self.__primero + 1) % self.__max
            self.__cant -= 1
            print(f"Elemento {elemento} suprimido")
            return elemento
        
    def recorrer(self):
        if not self.vacia():
            print("\nElementos de la lista:")
            i = self.__primero
            for j in range(self.__cant):
                print(f"[{j}] -> {self.__items[i]}")
                i = (i + 1) % self.__max # Para circular la cola.

    # La cola circular puede empezar en cualquier posición, no necesariamente en el índice 0 del arreglo.
    # Por eso self.__primero indica dónde está el primer elemento "real" de la cola, aunque su índice indique lo contrario.

        else:
            print("Cola vacía")
            
if __name__ == '__main__':
    tamaño = 5
    cola = ColaSecuencial(tamaño)
    cola.insertar(10)
    cola.insertar(20)
    cola.insertar(30)
    cola.insertar(40)
    cola.insertar(50)
    cola.recorrer()
    cola.suprimir()
    cola.recorrer()
    cola.insertar(60) # Si no se circulara la cola en recorrer, mostraría "60" en la primera posición física (0) del arreglo, cuando lógicamente no debería estar allí, rompiendo el orden FIFO.
    cola.insertar(70)
    cola.recorrer()