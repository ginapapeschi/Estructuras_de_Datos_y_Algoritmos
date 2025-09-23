import numpy as np

class ListaSecuencial:
    __elementos: np.ndarray
    __cant: int
    __max: int

    def __init__(self, max):
        self.__cant = 0
        self.__max = max
        self.__elementos = np.full(max, None, dtype=object)

    def vacia(self):
        return self.__cant == 0
    
    def llena(self):
        return self.__cant == self.__max
    
    def getSiguiente(self, pos):
        if 0 <= pos < self.__cant - 1:
            return self.__elementos[pos + 1]

        else: print("Posición fuera de rango"); return None
        
    def getAnterior(self, pos):
        if 0 < pos < self.__cant:
            return self.__elementos[pos - 1]
        
        else: print("Posición fuera de rango"); return None

    def getPrimerElemento(self):
        if not self.vacia():
            return self.__elementos[0]
        else: print("Lista vacía"); return None

    def getUltimoElemento(self):
        if not self.vacia():
            return self.__elementos[self.__cant - 1]
        else: print("Lista vacía"); return None
        
    def insertar(self, elemento):
        if not self.llena():
            self.__elementos[self.__cant] = elemento
            self.__cant += 1
            print(f"Elemento {elemento} insertado")
        else: print("Lista llena")
        
    def insertarPorPosicion(self, elemento, pos):
        if not self.llena():
            if 0 <= pos <= self.__cant:
                for i in range(self.__cant, pos, -1):
                    self.__elementos[i] = self.__elementos[i - 1]
                self.__elementos[pos] = elemento
                self.__cant += 1
                print(f"Elemento {elemento} insertado en la posición {pos}")
            else: print("Posición fuera de rango")
        else: print("Lista llena")

    def recorrer(self):
        if not self.vacia():
            print("\nElementos en la lista: ")
            for i in range(self.__cant):
                print(f"[{i}] -> {self.__elementos[i]}")
        
        else: print("Lista vacía")
    
    def suprimirPorPosicion(self, pos):
        if 0 <= pos < self.__cant:
            eliminado = self.__elementos[pos]
            for i in range(pos, self.__cant - 1):
                self.__elementos[i] = self.__elementos[i + 1]

            self.__elementos[self.__cant - 1] = None
            self.__cant -= 1
            print(f"Elemento en la posición {pos} eliminado: {eliminado}")
        
        else: print("Posición fuera de rango")

    def recuperar(self, pos):
        if 0 <= pos < self.__cant:
                return self.__elementos[pos]
        else: print("Posición fuera de rango"); return None
    
    def buscar(self, elemento):
        i = 0
        while i < self.__cant:
            if self.__elementos[i] == elemento:
                return i
            i += 1
        
        return -1

if __name__ == "__main__":
    lista = ListaSecuencial(5)
    lista.insertar(10)
    lista.insertar(20)
    lista.insertar(30)
    lista.recorrer()
    lista.insertarPorPosicion(40, 2)
    lista.recorrer()
    lista.insertarPorPosicion(50, 4)
    lista.recorrer()
    lista.suprimirPorPosicion(1)
    lista.recorrer()