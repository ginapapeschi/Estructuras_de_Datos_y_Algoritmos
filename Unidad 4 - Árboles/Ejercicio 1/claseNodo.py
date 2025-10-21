class Nodo:
    __valor: int
    __izq: object
    __der: object

    def __init__(self, valor):
        self.__valor = valor
        self.__izq = None
        self.__der = None

    def getValor(self):
        return self.__valor
    
    def setValor(self, valor):
        self.__valor = valor
    
    def getIzq(self):
        return self.__izq
    
    def setIzq(self, izq):
        self.__izq = izq

    def getDer(self):
        return self.__der
    
    def setDer(self, der):
        self.__der = der
