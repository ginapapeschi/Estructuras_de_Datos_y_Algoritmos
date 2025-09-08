import numpy as np

class Lista: 
    __elementos: np.ndarray
    __primero: int
    __ultimo: int
    __cant: int
    __max: int
    
    def __init__(self, max):
        self.__cant = 0
        self.__max = max
        self.__elementos = np.empty(max, dtype=object)
        self.__primero = -1
        self.__ultimo = -1
    
    def getPrimero(self):
        return self.__primero
    
    def getUltimo(self):
        return self.__ultimo
    
    def getSiguiente(self, pos):
        if self.__elementos[pos + 1]:
            return self.__elementos[pos + 1]
        
        else:
            return False
    
    def getAnterior(self, pos):
        if self.__elementos[pos - 1]:
            return self.__elementos[pos - 1]
        
        else:
            return False

    def vacia(self):
        return self.__cant == 0

    def llena(self):
        return self.__cant == self.__max

    def insertarPorPosicion(self, elemento, pos):
        if not self.llena():
            if 0 <= pos < self.__max:
                # Caso especial: primer elemento
                if self.__cant == 0 and pos == 0:
                    self.__elementos[0] = elemento
                    self.__cant = 1
                    self.__primero = 0
                    self.__ultimo = 0
                    print(f"Elemento {elemento} insertado en la posición {pos} (primer elemento)")

                # Sobrescribir en posición ya ocupada
                elif pos < self.__cant and self.__elementos[pos] != 0:
                    self.__elementos[pos] = elemento
                    print(f"Elemento {elemento} insertado en la posición {pos} (sobrescrito)")

                # Insertar nuevo en posición contigua exacta
                elif pos == self.__cant:
                    self.__elementos[pos] = elemento
                    self.__cant += 1
                    self.__ultimo = pos
                    print(f"Elemento {elemento} insertado en la posición {pos} (nuevo contiguo)")
                    

            else: # Cualquier otro caso rompe contigüidad
                print(f"{elemento} no se puede insertar: posición {pos} no contigua")
        else:
            print("Lista llena")

    def recorrer(self):
        if not self.vacia():
            print("\nElementos en la lista:")
            for i in range(self.__cant):
                print(f"[{i}] -> {self.__elementos[i]}")
        else:
            print("Lista vacía")
            
    def suprimirPorPosicion(self, pos):
        if 0 <= pos < self.__cant:
            print(f"Eliminando elemento en posición {pos}: {self.__elementos[pos]}")
            # Shift hacia la izquierda desde pos
            for i in range(pos, self.__cant - 1):
                self.__elementos[i] = self.__elementos[i + 1]
            # Limpia la última posición ahora duplicada
            self.__elementos[self.__cant - 1] = 0
            self.__cant -= 1

            # Actualiza punteros
            if self.__cant == 0:
                self.__primero = -1
                self.__ultimo = -1
            else:
                self.__ultimo = self.__cant - 1

            print("Elemento eliminado y elementos shifteados")
        else:
            print("Posición fuera de rango")



# Prueba
if __name__ == "__main__":
    lista = Lista(5)
    
    lista.insertarPorPosicion(10, 0)
    lista.insertarPorPosicion(20, 1)
    lista.insertarPorPosicion(30, 2)
    lista.insertarPorPosicion(1, 1)
    lista.insertarPorPosicion(40, 4)
    lista.insertarPorPosicion(35, 3)
    lista.insertarPorPosicion(99, 4)
    lista.insertarPorPosicion(2, 5)
    lista.insertarPorPosicion(2, 6)
    lista.suprimirPorPosicion(4)
    lista.insertarPorPosicion(2, 5)

    lista.recorrer()
