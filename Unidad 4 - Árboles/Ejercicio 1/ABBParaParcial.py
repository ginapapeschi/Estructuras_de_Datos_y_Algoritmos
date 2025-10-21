from claseNodo import Nodo

class Arbol:
    __raiz: Nodo
    
    def __init__(self):
        self.__raiz = None
    
    def vacia(self):
        return self.__raiz == None

    def getRaiz(self):
        return self.__raiz

    def setRaiz(self, nodo):
        self.__raiz = nodo
    
    def insertar(self, nodo, valor):
        if self.vacia():
            self.__raiz = Nodo(valor)
            print(f"Raíz creada - Valor {valor}")
        
        elif nodo.getValor() == valor:
            print("El nodo que se quiere insertar ya existe")

        elif valor < nodo.getValor():
            if nodo.getIzq():
                self.insertar(nodo.getIzq(), valor)
            else:
                nodo.setIzq(Nodo(valor))
                print(f"Nodo izquierdo insertado - Valor: {valor}")
        
        else:
            if nodo.getDer():
                self.insertar(nodo.getDer(), valor)
            else:
                nodo.setDer(Nodo(valor))
                print(f"Nodo derecho insertado - Valor: {valor}")
        
    def suprimir(self, nodo, valor):
        resultado = nodo
        if nodo:
            if valor < nodo.getValor():
                nodo.setIzq(self.suprimir(nodo.getIzq(), valor))
            elif valor > nodo.getValor():
                nodo.setDer(self.suprimir(nodo.getDer(), valor))
            else:
                grado = self.grado(nodo)
                if grado == 0: # Nodo hoja.
                    resultado = None
                elif grado == 1: # Nodo con un hijo, da el existente.
                    if nodo.getDer():
                        resultado = nodo.getDer()
                    else: 
                        resultado = nodo.getIzq()
                else: # Grado == 2, nodo con dos hijos. Usa el máximo del subárbol izquierdo.
                    maximo = nodo.getIzq()
                    while maximo.getDer():
                        maximo = maximo.getDer()
                    nodo.setValor(maximo.getValor())
                    nodo.setIzq(self.suprimir(nodo.getIzq(), maximo.getValor()))
                    resultado = nodo

        if nodo == self.__raiz:
            self.setRaiz(resultado) # Actualiza la raíz si el nodo a eliminar era la raíz.
        return resultado # Devuelve el nodo modificado

    def inOrden(self, nodo):    # Hijo, padre, hijo (izq - raíz - der).
        if nodo:
            self.inOrden(nodo.getIzq())
            print(nodo.getValor())
            self.inOrden(nodo.getDer())

    def preOrden(self, nodo):   # Primero padre, luego hijos (raíz - izq - der).
        if nodo:
            print(nodo.getValor())  
            self.preOrden(nodo.getIzq())
            self.preOrden(nodo.getDer())
    
    def postOrden(self, nodo):  # Primero hijos, después el padre (izq - der - raíz).
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
            if nodo.getValor() == antecesor: # Se encontró el nodo que podría ser antecesor.
                encontrado = self.buscar(nodo, valor) # Se verifica si el valor buscado está en su subárbol.
                if encontrado:
                    resultado = True
            else: # Se sigue buscando en subárboles.
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
        nodoPadre = self.buscar(self.getRaiz(), padre)
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
            if nodo.getIzq() and nodo.getIzq().getValor() == valor: # El valor está en el hijo izquierdo.
                padre = nodo.getValor()
                if nodo.getDer():
                    hermano = nodo.getDer().getValor()

            elif nodo.getDer() and nodo.getDer().getValor() == valor: # El valor está en el hijo derecho.
                padre = nodo.getValor()
                if nodo.getIzq():
                    hermano = nodo.getIzq().getValor()

            elif valor < nodo.getValor():
                p, h = self.padreHermano(nodo.getIzq(), valor) # Recursión en subárbol izquierdo.
                if p:
                    padre, hermano = p, h
            
            elif valor > nodo.getValor():
                p, h = self.padreHermano(nodo.getDer(), valor) # Recursión en subárbol derecho.
                if p:
                    padre, hermano = p, h
        return padre, hermano

    def hoja(self, valor):
        nodo = self.buscar(self.getRaiz(), valor)
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
            if nodo.getValor() == valor:
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
                    camino.append(0) # Va a la izquierda
                    nodoActual = nodoActual.getIzq()
                else:
                    camino.append(1) # Va a la derecha
                    nodoActual = nodoActual.getDer()
        return camino
    
    def cantidadNodos(self, nodo, cant):
        if nodo:
            cant = self.cantidadNodos(nodo.getIzq(), cant)
            cant += 1
            cant = self.cantidadNodos(nodo.getDer(), cant)
        return cant

'''
if __name__ == '__main__':
    arbol = Arbol()
    arbol.insertar(arbol.getRaiz(), 10)
    arbol.insertar(arbol.getRaiz(), 5)
    arbol.insertar(arbol.getRaiz(), 3)
    arbol.insertar(arbol.getRaiz(), 7)
    arbol.insertar(arbol.getRaiz(), 20)
    arbol.insertar(arbol.getRaiz(), 8)
    arbol.insertar(arbol.getRaiz(), 9)
    print("Inorden:")
    arbol.inOrden(arbol.getRaiz())
    print("PreOrden:")
    arbol.preOrden(arbol.getRaiz())
    print("PostOrden:")
    arbol.postOrden(arbol.getRaiz())
    encontrado = arbol.buscar(arbol.getRaiz(), 3)
    if encontrado:
        print(f"Valor encontrado: {encontrado.getValor()}")
    else:
        print("No se encontró el valor en el árbol")
    
    nivel = arbol.nivel(arbol.getRaiz(), 10)
    if nivel != -1:
        print(f"Nivel del nodo 10: {nivel}")
    else: print("El nodo con el valor ingresado no se encuentra en el árbol")
    print(f"Altura del árbol: {arbol.altura(arbol.getRaiz())}")

    antecesor = arbol.antecesor(arbol.getRaiz(), 10, 3)
    if antecesor:
        print("Es antecesor")
    else:
        print("No es antecesor")
    
    camino = (arbol.camino(10, 3))
    if camino:
        print(f"Camino: {camino}")
    else:
        print("No existe camino: el inicio no es antecesor del fin")

    print("\nSucesores:")
    arbol.sucesores(5)

    print("\nÁrbol antes de eliminar:")
    arbol.preOrden(arbol.getRaiz())
    arbol.suprimir(arbol.getRaiz(), 3)
    print("Árbol tras eliminar:")
    arbol.preOrden(arbol.getRaiz())
    print(f"Raíz del árbol: {arbol.getRaiz().getValor()}")
    print("Eliminando la raíz")
    arbol.suprimir(arbol.getRaiz(), 10)
    print(f"Nueva raíz: {arbol.getRaiz().getValor()}")
    print("Árbol tras eliminar la raíz:")
    arbol.preOrden(arbol.getRaiz())
'''