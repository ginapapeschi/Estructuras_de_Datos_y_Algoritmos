from claseNodo import Nodo

class Arbol:
    __raiz: Nodo
    
    def __init__(self):
        self.__raiz = None
    
    def vacia(self):
        return self.__raiz == None

    def getRaiz(self):
        return self.__raiz
    
    def insertar(self, valor):
        if not self.__raiz:
            self.__raiz = Nodo(valor)
            print(f"Raíz creada - Valor {valor}")
        else:
            self.insertarNodo(self.__raiz, valor)

    def insertarNodo(self, nodo, valor):
        if nodo.getValor() == valor:
            print("El nodo que se quiere insertar ya existe")
        
        elif valor < nodo.getValor():
            if nodo.getIzq():
                self._insertar(nodo.getIzq(), valor)
            else:
                nodo.setIzq(Nodo(valor))
                #print(f"Nodo insertado - Valor: {valor}")
        
        else:
            if nodo.getDer():
                self._insertar(nodo.getDer(), valor)
            else:
                nodo.setDer(Nodo(valor))
                #print(f"Nodo insertado - Valor: {valor}")
        
    def suprimir(self, valor):
        self.__raiz = self.suprimirNodo(self.__raiz, valor)
    
    def suprimirNodo(self, nodo, valor):
        if not nodo:
            return None
        
        elif nodo.getValor() > valor:
            nodo.setIzq(self.suprimirNodo(nodo.getIzq(), valor))
        
        elif nodo.getValor() < valor:
            nodo.setDer(self.suprimirNodo(nodo.getDer(), valor))
        
        else:
            if self.grado(nodo) == 0:
                return None
            if self.grado(nodo) == 1:
                if nodo.getDer():
                    return nodo.getDer()
                else:
                    return nodo.getIzq()
            
            if self.grado(nodo) == 2:
                maximo = nodo.getIzq()
                while maximo.getDer() != None:
                    maximo = maximo.getDer()
                nodo.setValor(maximo.getValor())
                nodo.setIzq(self.suprimirNodo(nodo.getIzq(), maximo.getValor()))
        
        return nodo

    def inOrden(self):
        self.inOrdenNodo(self.__raiz)
    
    def inOrdenNodo(self, nodo):   # Hijo, padre, hijo (izq - raíz - der).
        if nodo:
            self.inOrdenNodo(nodo.getIzq())
            print(nodo.getValor())
            self.inOrdenNodo(nodo.getDer())

    def preOrden(self):
        self.preOrdenNodo(self.__raiz)
    
    def preOrdenNodo(self, nodo):  # Primero padre, luego hijos (raíz - izq - der).
        if nodo:
            print(nodo.getValor())  
            self.preOrdenNodo(nodo.getIzq())
            self.preOrdenNodo(nodo.getDer())
    
    def postOrden(self):
        self.postOrdenNodo(self.__raiz)
    
    def postOrdenNodo(self, nodo): # Primero hijos, después el padre (izq - der - raíz).
        if nodo:
            self.postOrdenNodo(nodo.getIzq())
            self.postOrdenNodo(nodo.getDer())
            print(nodo.getValor())

    def buscar(self, valor):
        return self.buscarNodo(self.__raiz, valor)

    def buscarNodo(self, nodo, valor):
        if not nodo:
            nodoEncontrado = None
        elif nodo.getValor() == valor:
            nodoEncontrado = nodo
        elif nodo.getValor() > valor:
            nodoEncontrado = self.buscarNodo(nodo.getIzq(), valor)
        else:
            nodoEncontrado = self.buscarNodo(nodo.getDer(), valor)
        return nodoEncontrado

    def antecesor(self, antecesor, valor):
        return self.verificarAntecesor(self.__raiz, antecesor, valor, False)
    
    def verificarAntecesor(self, nodo, antecesor, valor, encontrado):
        esAntecesor = False
        if nodo:
            if antecesor == nodo.getValor():
                encontrado = True
            
            if valor == nodo.getValor():
                if encontrado and antecesor != valor:
                    esAntecesor = True
            
            elif valor < nodo.getValor():
                esAntecesor = self.verificarAntecesor(nodo.getIzq(), antecesor, valor, encontrado)
            
            else:
                esAntecesor = self.verificarAntecesor(nodo.getDer(), antecesor, valor, encontrado)
        return esAntecesor
    
    def padre(self, padre, hijo):
        nodoPadre = self.buscar(padre)
        esPadre = False
        if nodoPadre:
            if nodoPadre.getIzq() != None and nodoPadre.getIzq().getValor() == hijo:
                esPadre = True
            elif nodoPadre.getDer() != None and nodoPadre.getDer().getValor() == hijo:
                esPadre = True
        return esPadre
    
    def hijo(self, hijo, padre):
        nodoPadre = self.buscar(padre)
        esHijo = False
        if nodoPadre:
            if nodoPadre.getIzq() != None and nodoPadre.getIzq().getValor() == hijo:
                esHijo = True
            elif nodoPadre.getDer() != None and nodoPadre.getDer().getValor() == hijo:
                esHijo = True
        return esHijo

    def hoja(self, valor):
        nodo = self.buscar(valor)
        return nodo is not None and self.grado(nodo) == 0
            
    def grado(self, nodo):
        grado = 0
        if nodo.getIzq():
            grado += 1
        if nodo.getDer():
            grado += 1
        return grado
    
    def nivel(self, valor):
        return self.calcularNivel(self.__raiz, valor, 1)

    def calcularNivel(self, nodo, valor, nivel):
        resultado = 0
        if nodo:
            if nodo.getValor() > valor:
                resultado = self.calcularNivel(nodo.getIzq(), valor, nivel + 1)
            elif nodo.getValor() < valor:
                resultado = self.calcularNivel(nodo.getDer(), valor, nivel + 1)
            else:
                resultado = nivel
        return resultado
    
    def altura(self):
        return self.calcularAltura(self.__raiz)
    
    def calcularAltura(self, nodo):
        maxAltura = 0
        if nodo:
            alturaIzq = self.calcularAltura(nodo.getIzq())
            alturaDer = self.calcularAltura(nodo.getDer())
            maxAltura = 1 + max(alturaIzq, alturaDer)
        return maxAltura

    def camino(self, inicio, fin):
        esAntecesor = self.antecesor(inicio, fin)
        camino = []
        if esAntecesor:
            nodoActual = self.buscar(inicio)
            while nodoActual != None and nodoActual.getValor() != fin:
                if fin < nodoActual.getValor():
                    camino.append(0) # Va a la izquierda
                    nodoActual = nodoActual.getIzq()
                else:
                    camino.append(1) # Va a la derecha
                    nodoActual = nodoActual.getDer()
        
        return camino
    
if __name__ == '__main__':
    arbol = Arbol()
    arbol.inOrden()
    arbol.insertar(10)
    arbol.insertar(5)
    arbol.insertar(3)
    arbol.insertar(7)
    arbol.insertar(20)
    #print("Inorden:")
    #arbol.inOrden()
    #print("PreOrden:")
    #arbol.preOrden()
    #print("PostOrden:")
    #arbol.postOrden()
    encontrado = arbol.buscar(3)
    if encontrado:
        print(f"Valor encontrado: {encontrado.getValor()}")
    else:
        print("No se encontró el valor en el árbol")
    print(f"Nivel del nodo 10: {arbol.nivel(10)}")
    print(f"Nivel del nodo 15: {arbol.nivel(15)}")
    print(f"Nivel del nodo 3: {arbol.nivel(3)}")
    print(f"Altura del árbol: {arbol.altura()}")
    antecesor = arbol.antecesor(10, 3)
    if antecesor:
        print("Es antecesor")
    else:
        print("No es antecesor")
    
    print(arbol.camino(10, 3))
    #print("Árbol antes de eliminar:")
    #arbol.preOrden()
    arbol.suprimir(3)
    #print("Árbol tras eliminar:")
    #arbol.preOrden()
    print(f"{arbol.getRaiz().getValor()}")
    arbol.suprimir(10)
    print(f"{arbol.getRaiz().getValor()}")

    arbol.mostrar(arbol.getRaiz())