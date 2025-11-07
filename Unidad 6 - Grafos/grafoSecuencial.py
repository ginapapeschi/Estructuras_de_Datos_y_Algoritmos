import numpy as np

class Celda:
    __elemento: str
    __siguiente: str

    def __init__(self, elemento):
        self.__elemento = elemento
        self.__siguiente = None
    
    def getElemento(self):
        return self.__elemento
    
    def setElemento(self, elemento):
        self.__elemento = elemento

    def getSiguiente(self):
        return self.__siguiente
    
    def setSiguiente(self, sig):
        self.__siguiente = sig

class Cola:
    __primero: Celda
    __ultimo: Celda
    __cant: int
    
    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, elemento):
        nuevo = Celda(elemento)
        if self.vacia():
            self.__primero = nuevo
        else:
            self.__ultimo.setSiguiente(nuevo)
        self.__ultimo = nuevo
        self.__cant += 1

    def suprimir(self):
        if self.vacia():
            print("Cola vacía")
        else:
            eliminado = self.__primero.getElemento()
            self.__cant -= 1
            self.__primero = self.__primero.getSiguiente()
            return eliminado
    
    def recuperar(self):
        return self.__primero
    
class Pila:
    __tope: Celda
    __cant: int

    def __init__(self):
        self.__tope = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, elemento):
        nuevo = Celda(elemento)
        nuevo.setSiguiente(self.__tope)
        self.__tope = nuevo
        self.__cant += 1
    
    def suprimir(self):
        self.__cant -= 1
        eliminado = self.__tope.getElemento()
        self.__tope = self.__tope.getSiguiente()
        return eliminado
    
class Grafo:
    __tamaño: int
    __matriz: np.array
    __vertices: str

    def __init__(self, tamaño):
        self.__tamaño = tamaño
        self.__matriz = np.zeros((tamaño, tamaño), dtype=int)
        self.__vertices = "ABCD"

    def insertar(self, verticeInicial, verticeFinal):
        indiceInicial = self.__vertices.index(verticeInicial)
        indiceFinal = self.__vertices.index(verticeFinal)
        if self.__matriz[indiceInicial][indiceFinal] == 0:
            self.__matriz[indiceInicial][indiceFinal] = 1
            self.__matriz[indiceFinal][indiceInicial] = 1
        else:
            print("Ya hay una relación entre los vértices ingresados")
    
    def suprimir(self, verticeInicial, verticeFinal):
        indiceInicial = self.__vertices.index(verticeInicial)
        indiceFinal = self.__vertices.index(verticeFinal)
        if self.__matriz[indiceInicial][indiceFinal] == 1:
            self.__matriz[indiceInicial][indiceFinal] = 0
            self.__matriz[indiceFinal][indiceInicial] = 0
        else:
            print("No hay una relación entre los vértices ingresados")
            
    def mostrar(self):
        print(self.__matriz)
    
        # Igual que en grafo.
    def adyacentes(self, vertice):
        indiceVertice = self.__vertices.index(vertice)
        adyacentes = []
        for j in range(self.__tamaño):
            if self.__matriz[indiceVertice][j] == 1:
                adyacentes.append(self.__vertices[j])
        return adyacentes
    
    # Igual que en grafo.
    def busquedaEnAnchura(self, vertice):
        cola = Cola()
        indiceVertice = self.__vertices.index(vertice)
        visitados = [float('inf')] * self.__tamaño
        visitados[indiceVertice] = 0
        cola.insertar(vertice)
        print(vertice)
        while not cola.vacia():
            actual = cola.suprimir()
            indiceActual = self.__vertices.index(actual)
            vecinos = ""
            for vecino in self.adyacentes(actual):
                indiceVecino = self.__vertices.index(vecino)
                if visitados[indiceVecino] == float('inf'):
                    visitados[indiceVecino] = visitados[indiceActual] + 1
                    cola.insertar(vecino)
                    vecinos += vecino + " "
            # Sólo de BEA.
            if vecinos != "":
                print(vecinos)
    
    # Igual que en grafo.
    def caminoMinimo(self, verticeInicial, verticeFinal):
        cola = Cola()
        indiceVertice = self.__vertices.index(verticeInicial)
        visitados = [float('inf')] * self.__tamaño
        visitados[indiceVertice] = 0
        predecesores = [None] * self.__tamaño
        cola.insertar(verticeInicial)
        while not cola.vacia():
            actual = cola.suprimir()
            indiceActual = self.__vertices.index(actual)
            for vecino in self.adyacentes(actual):
                indiceVecino = self.__vertices.index(vecino)
                if visitados[indiceVecino] == float('inf'):
                    visitados[indiceVecino] = visitados[indiceActual] + 1
                    cola.insertar(vecino)
                    predecesores[indiceVecino] = actual
        camino = Pila()
        actual = verticeFinal
        if predecesores[self.__vertices.index(actual)]:
            while actual:
                camino.insertar(actual)
                actual = predecesores[self.__vertices.index(actual)]
            while not camino.vacia():
                print(camino.tope())
                camino.suprimir()
        else:
            print(f"No existe un camino desde {verticeInicial} hasta {verticeFinal}")

    # ESTUDIAR ESTE
    def caminoEntreNodos(self, u, v):
        visitados = []
        camino = []
        band = True
        if self.busquedaEnAmplitud(u, v, camino, visitados):
            print(f"Camino de {u} a {v}:", end=" ")
            for i in camino:
                print(f"[{i}]", end=" ")
                band = True
        else:
            print(f"No existe camino de {u} a {v}")
            band = False
        return band
    
    # ESTUDIAR ESTE
    def busquedaEnAmplitud(self, u, v, camino, visitados):
        cola = Cola()
        predecesor = {}
        cola.insertar(u)
        visitados.append(u)
        encontrado = False

        while not cola.vacia() and not encontrado:
            actual = cola.suprimir()

            if actual == v:
                encontrado = True
            else:
                for adyacente in self.adyacentes(actual):
                    if adyacente not in visitados:
                        visitados.append(adyacente)
                        predecesor[adyacente] = actual
                        cola.insertar(adyacente)

        if encontrado:
            # reconstrucción del camino desde v hacia u
            actual = v
            while actual is not None:
                camino.insert(0, actual)
                actual = predecesor.get(actual)

        return encontrado

    # Igual que en grafo.
    def BEPVisita(self, indiceVertice, descubrimiento, fin, tiempo):
        tiempo[0] += 1
        descubrimiento[indiceVertice] = tiempo[0]
        for u in range(self.__tamaño):
            if self.__matriz[indiceVertice][u] == 1 and descubrimiento[u] == 0:
                self.BEPVisita(u, descubrimiento, fin, tiempo)
        tiempo[0] += 1
        fin[indiceVertice] = tiempo[0]
    
    # Igual que en grafo.
    def busquedaEnProfundidad(self, vertice):
        descubrimiento = [0] * self.__tamaño
        fin = [0] * self.__tamaño
        tiempo = [0]
        indiceVertice = self.__vertices.index(vertice)
        if descubrimiento[indiceVertice] == 0:
            self.BEPVisita(indiceVertice, descubrimiento, fin, tiempo)
    
        for i in range(self.__tamaño):
            print(f"{self.__vertices[i]}: descubrimiento = {descubrimiento[i]}, fin = {fin[i]}")
        return descubrimiento, fin
    
    # Igual que en grafo.
    def esConexo(self):
        descubrimiento, _ = self.busquedaEnProfundidad(self.__vertices[0]) # Empieza desde el primer vértice.
        resultado = True
        for valor in descubrimiento:
            if valor == 0:
                resultado = False
        return resultado
    
    # Igual que en grafo
    def esAciclico(self):
        _, _, clasificacion = self.BEPClasificacion(self.__vertices[0])
        esAciclico = True
        i = 0
        while i < len(clasificacion):
            _, _, tipo = clasificacion[i]
            if tipo == 'arista hacia atrás':
                esAciclico = False
            i += 1
        return esAciclico
    
    # Igual que en grafo.
    def BEPClasificacion(self, string):
        descubrimiento = [0] * self.__tamaño
        fin = [0] * self.__tamaño
        tiempo = [0]
        clasificacion = []
        indiceString = self.__vertices.index(string)
        if descubrimiento[indiceString] == 0:
            self.BEPVisitaClasificacion(indiceString, descubrimiento, fin, tiempo, clasificacion)
        return descubrimiento, fin, clasificacion
    
    # Igual que en grafo.
    def BEPVisitaClasificacion(self, indiceVertice, descubrimiento, fin, tiempo, clasificacion):
        tiempo[0] += 1
        descubrimiento[indiceVertice] = tiempo[0]
        for u in range(self.__tamaño):
            if self.__matriz[indiceVertice][u] == 1:
                if descubrimiento[u] == 0:
                    clasificacion.append((self.__vertices[indiceVertice], self.__vertices[u], "arista de árbol"))
                    self.BEPVisitaClasificacion(u, descubrimiento, fin, tiempo, clasificacion)
                elif fin[u] == 0:
                    clasificacion.append((self.__vertices[indiceVertice], self.__vertices[u], "arista hacia atrás"))
        tiempo[0] += 1
        fin[indiceVertice] = tiempo[0]
