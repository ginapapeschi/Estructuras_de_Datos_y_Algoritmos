class Celda:
    __item: int
    __sig: int

    def __init__(self, item):
        self.__item = item
        self.__sig = None
    
    def getItem(self):
        return self.__item
    
    def setItem(self, item):
        self.__item = item

    def getSiguiente(self):
        return self.__sig
    
    def setSiguiente(self, siguiente):
        self.__sig = siguiente

class ColaEncadenada:
    __primero: object
    __ultimo: object
    __cant: int

    def __init__(self, primero=None, ultimo=None):
        self.__primero = 0
        self.__ultimo = 0
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, elemento):
        nuevo = Celda()
        nuevo.setItem(elemento)
        nuevo.setSiguiente(None)

        if self.__ultimo is None:
            self.__primero = nuevo
        else:
            self.__ultimo.setSiguiente(nuevo)

        self.__ultimo = nuevo
        self.__cant += 1
        return self.__ultimo.getItem()
    
    def suprimir(self):
        if self.vacia():
            print("Cola vacía")
            return None
        
        else:
            actual = self.__primero
            elemento = actual.getItem()
            self.__primero = actual.getSiguiente()
            self.__cant -= 1

            if self.__primero is None:
                self.__ultimo = None
            
            del actual
            return elemento
    
    def getPrimero(self):
        return self.__primero

    def recorrer(self, actual=None):
        if actual is None:
            actual = self.__primero
        
        if actual is not None:
            print(actual.getItem())
            self.recorrer(actual.getSiguiente())