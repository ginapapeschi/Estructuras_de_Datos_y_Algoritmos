class Celda:
    __elemento: int
    __sig: int

    def __init__(self, elemento):
        self.__elemento = elemento
        self.__sig = None

    def getElemento(self):
        return self.__elemento
    
    def getSiguiente(self):
        return self.__sig
    
    def setElemento(self, elemento):
        self.__elemento = elemento

    def setSiguiente(self, siguiente):
        self.__sig = siguiente

class PilaEncadenada:
    __tope: Celda
    __cant: int

    def __init__(self):
        self.__tope = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0
    
    def getCantidad(self):
        return self.__cant
    
    def getTope(self):
        return self.__tope
    
    def insertar(self, elemento):
        nuevaCelda = Celda(elemento)
        nuevaCelda.setSiguiente(self.__tope)
        self.__tope = nuevaCelda
        self.__cant += 1
        print(f"Elemento {elemento} insertado")
    
    def suprimir(self):
        if self.vacia():
            print("Pila vacía")
        
        else:
            actual = self.__tope
            elemento = actual.getElemento()
            self.__tope = actual.getSiguiente()
            self.__cant -= 1
            return elemento
        
    def mostrar(self):
        if not self.vacia():
            actual = self.__tope
            print("\nContenido de la pila:")
            i = 0
            while actual != None:
                print(f"[{i}] -> {actual.getElemento()}")
                actual = actual.getSiguiente()
                i += 1
        
        else:
            print("Pila vacía")

if __name__ == '__main__':
    pila = PilaEncadenada()
    pila.insertar(1)
    pila.insertar(2)
    pila.insertar(3)
    pila.insertar(4)
    pila.insertar(5)
    pila.insertar(6)
    pila.mostrar()
    borrado = pila.suprimir()
    print(f"Elemento borrado: {borrado}")
    pila.mostrar()
    pila.insertar(7)
    pila.mostrar()