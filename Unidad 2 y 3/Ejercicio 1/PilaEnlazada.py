class Celda:
    __item: int
    __sig: object

    def __init__(self):
        self.__item = None
        self.__sig = None

    def getItem(self):
        return self.__item
    
    def setItem(self, elemento):
        self.__item = elemento

    def setSiguiente(self, tope):
        self.__sig = tope
    
    def getSiguiente(self):
        return self.__sig
    
class PilaEnlazada:
    __tope: object
    __cant: int

    def __init__(self):
        self.__tope = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, elemento):
        nuevaCelda = Celda()
        nuevaCelda.setItem(elemento)
        nuevaCelda.setSiguiente(self.__tope)
        self.__tope = nuevaCelda
        self.__cant += 1
        print(f"Elemento {elemento} insertado")

    def suprimir(self):
        if self.vacia():
            print("Pila vacía")
        else:
            actual = self.__tope
            elemento = actual.getItem()
            self.__tope = actual.getSiguiente()
            self.__cant -= 1
            print(f"Elemento {elemento} eliminado")

    def mostrar(self):
        actual = self.__tope
        print("Contenido de la pila:")
        while actual is not None:
            print(actual.getItem())
            actual = actual.getSiguiente()

if __name__ == '__main__':
    pila = PilaEnlazada()
    pila.insertar(10)
    pila.insertar(20)
    pila.insertar(30)
    pila.insertar(40)
    pila.insertar(50)
    pila.insertar(60)
    pila.mostrar()
    pila.suprimir()
    pila.mostrar()