class Nodo:
    __valor: int
    __izq: int
    __der: int
    __sig: int

    def __init__(self, valor):
        self.__valor = valor
        self.__izq = None
        self.__der = None
        self.__sig = None
    
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

    def getSiguiente(self):
        return self.__sig

    def setSiguiente(self, sig):
        self.__sig = sig

class Arbol:
    __raiz: Nodo

    def __init__(self):
        self.__raiz = None
    
    def getRaiz(self):
        return self.__raiz
    
    def setRaiz(self, nodo):
        self.__raiz = nodo
    
    def vacia(self):
        return self.__raiz == None

    def insertar(self, nodo, valor):
        if self.vacia():
            self.__raiz = Nodo(valor)
        elif valor == nodo.getValor():
            print("El nodo que se quiere insertar ya existe")
        elif valor < nodo.getValor():
            if nodo.getIzq():
                self.insertar(nodo.getIzq(), valor)
            else:
                nodo.setIzq(Nodo(valor))
        else:
            if nodo.getDer():
                self.insertar(nodo.getDer(), valor)
            else:
                nodo.setDer(Nodo(valor))

    def suprimir(self, nodo, valor):
        resultado = nodo
        if nodo:
            if valor < nodo.getValor():
                nodo.setIzq(self.suprimir(nodo.getIzq(), valor))
            elif valor > nodo.getValor():
                nodo.setDer(self.suprimir(nodo.getDer(), valor))
            else:
                grado = self.grado(nodo)
                if grado == 0:
                    resultado = None
                elif grado == 1:
                    if nodo.getDer():
                        resultado = nodo.getDer()
                    else:
                        resultado = nodo.getIzq()
                elif grado == 2:
                    maximo = nodo.getIzq()
                    while maximo.getDer():
                        maximo = maximo.getDer()
                    nodo.setValor(maximo.getValor())
                    nodo.setIzq(self.suprimir(nodo.getIzq(), maximo.getValor()))
                    resultado = nodo
        if nodo == self.__raiz:
            self.setRaiz(resultado)
        return resultado
    
    def inOrden(self, nodo):
        if nodo:
            self.inOrden(nodo.getIzq())
            print(nodo.getValor())
            self.inOrden(nodo.getDer())
    
    def preOrden(self, nodo):
        if nodo:
            print(nodo.getValor())
            self.preOrden(nodo.getIzq())
            self.preOrden(nodo.getDer())
    
    def postOrden(self, nodo):
        if nodo:
            self.postOrden(nodo.getIzq())
            self.postOrden(nodo.getDer())
            print(nodo.getValor())

    def buscar(self, nodo, valor):
        if not nodo:
            nodoEncontrado = None
        elif nodo.getValor() == valor:
            nodoEncontrado = nodo
        elif valor < nodo.getValor():
            nodoEncontrado = self.buscar(nodo.getIzq(), valor)
        else:
            nodoEncontrado = self.buscar(nodo.getDer(), valor)
        return nodoEncontrado
    
    def antecesor(self, nodo, antecesor, valor):
        resultado = False
        if nodo:
            if nodo.getValor() == antecesor:
                encontrado = self.buscar(nodo, valor)
                if encontrado:
                    resultado = True
            else:
                if valor < nodo.getValor():
                    resultado = self.antecesor(nodo.getIzq(), antecesor, valor)
                else:
                    resultado = self.antecesor(nodo.getDer(), antecesor, valor)
        return resultado

    def sucesores(self, valor):
        nodo = self.buscar(self.__raiz, valor)
        if nodo:
            if nodo.getDer():
                self.preOrden(nodo.getDer())
            else:
                print(f"No hay sucesores de {valor}")
        else:
            print(f"El nodo con valor {valor} no existe en el árbol")
    
    def relacionPadreHijo(self, padre, hijo):
        resultado = False
        nodoPadre = self.buscar(self.__raiz, padre)
        if nodoPadre:
            if nodoPadre.getIzq() and nodoPadre.getIzq().getValor() == hijo:
                resultado = True
            if nodoPadre.getDer() and nodoPadre.getDer().getValor() == hijo:
                resultado = True
        return resultado

    def padre(self, padre, hijo):
        return self.relacionPadreHijo(padre, hijo)

    def hijo(self, hijo, padre):
        return self.relacionPadreHijo(padre, hijo)
    
    def padreHermano(self, nodo, valor):
        padre, hermano = None, None
        if nodo:
            if nodo.getIzq() and nodo.getIzq().getValor() == valor:
                padre = nodo.getValor()
                if nodo.getDer():
                    hermano = nodo.getDer().getValor()
            elif nodo.getDer() and nodo.getDer().getValor() == valor:
                padre = nodo.getValor()
                if nodo.getIzq():
                    hermano = nodo.getIzq().getValor()
            elif valor < nodo.getValor():
                p, h = self.padreHermano(nodo.getIzq(), valor)
                if p:
                    padre, hermano = p, h
            elif valor > nodo.getValor():
                p, h = self.padreHermano(nodo.getDer(), valor)
                if p:
                    padre, hermano = p, h
        return padre, hermano

    def hoja(self, valor):
        nodo = self.buscar(self.__raiz, valor)
        return nodo is not None and self.grado(nodo) == 0

    def grado(self, nodo):
        grado = 0
        if nodo.getIzq():
            grado += 1
        if nodo.getDer():
            grado += 1
        return grado
    
    def nivel(self, nodo, valor, nivel=1):
        resultado = -1
        if nodo:
            if valor == nodo.getValor():
                resultado = nivel
            elif valor < nodo.getValor():
                resultado = self.nivel(nodo.getIzq(), valor, nivel + 1)
            else:
                resultado = self.nivel(nodo.getDer(), valor, nivel + 1)
        return resultado
    
    def altura(self, nodo):
        maxAltura = 0 
        if nodo:
            alturaIzq = self.altura(nodo.getIzq())
            alturaDer = self.altura(nodo.getDer())
            maxAltura = 1 + max(alturaIzq, alturaDer)
        return maxAltura
    
    def camino(self, inicio, fin):
        esAntecesor = self.antecesor(self.__raiz, inicio, fin)
        camino = []
        if esAntecesor:
            nodoActual = self.buscar(self.__raiz, inicio)
            while nodoActual and nodoActual.getValor() != fin:
                if fin < nodoActual.getValor():
                    camino.append(0)
                    nodoActual = nodoActual.getIzq()
                else:
                    camino.append(1)
                    nodoActual = nodoActual.getDer()
        return camino
    
    def cantidadNodos(self, nodo, cant):
        if nodo:
            cant = self.cantidadNodos(nodo.getIzq(), cant)
            cant += 1
            cant = self.cantidadNodos(nodo.getDer(), cant)
        return cant
