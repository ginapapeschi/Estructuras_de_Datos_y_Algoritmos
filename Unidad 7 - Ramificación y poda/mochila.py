class Nodo:
    __nivel: int
    __peso: float
    __valor: float
    __bound: float
    __elementos: list

    def __init__(self, nivel, peso, valor, bound, elementos):
        self.__nivel = nivel
        self.__peso = peso
        self.__valor = valor
        self.__bound = bound
        self.__elementos = elementos

    def __lt__(self, otro):
        return self.__bound > otro.getBound()

    def getNivel(self):
        return self.__nivel
    
    def getPeso(self):
        return self.__peso
    
    def getValor(self):
        return self.__valor
    
    def getElementos(self):
        return self.__elementos

    def getBound(self):
        return self.__bound
    
    def setBound(self, bound):
        self.__bound = bound

class Celda:
    def __init__(self, item):
        self.__item = item
        self.__sig = None

    def getItem(self):
        return self.__item

    def getSiguiente(self):
        return self.__sig

    def setSiguiente(self, sig):
        self.__sig = sig

class ColaEncadenadaPrioridad:
    __primero: Nodo
    __cant: int

    def __init__(self):
        self.__primero = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0

    def recuperar(self):
        if not self.vacia():
            return self.__primero.getItem()

    def insertar(self, elemento):
        nuevo = Celda(elemento)
        if self.vacia() or elemento.getBound() > self.__primero.getItem().getBound():
            nuevo.setSiguiente(self.__primero)
            self.__primero = nuevo
        else:
            actual = self.__primero
            while (actual.getSiguiente() is not None and
                   actual.getSiguiente().getItem().getBound() >= elemento.getBound()):
                actual = actual.getSiguiente()
            nuevo.setSiguiente(actual.getSiguiente())
            actual.setSiguiente(nuevo)
        self.__cant += 1
        return elemento

    def suprimir(self):
        if self.vacia():
            print("Cola vacía")
            return None
        elemento = self.__primero.getItem()
        self.__primero = self.__primero.getSiguiente()
        self.__cant -= 1
        return elemento

def calcularCota(nodo, pesos, valores, capacidad):
    if nodo.getPeso() >= capacidad:
        return 0
    valorBound = nodo.getValor()
    j = nodo.getNivel() + 1
    pesoTotal = nodo.getPeso()
    while j < len(pesos) and pesoTotal + pesos[j] <= capacidad:
        pesoTotal += pesos[j]
        valorBound += valores[j]
        j += 1
    if j < len(pesos):
        valorBound += (capacidad - pesoTotal) * valores[j] / pesos[j]
    return valorBound

def claveOrden(item):
    return item[2]

def ramificacionYPoda(pesos, valores, capacidad):
    # --- 1. Preprocesamiento: ordenar por densidad (valor/peso) descendente ---
    valorPorPeso = []
    for i in range(len(valores)):
        valor = valores[i]
        peso = pesos[i]
        densidad = valor / peso
        valorPorPeso.append(densidad)
    
    items = []
    for i in range(len(pesos)):
        peso = pesos[i]
        valor = valores[i]
        vpp = valorPorPeso[i]
        items.append((peso, valor, vpp, i))
    items.sort(key=claveOrden, reverse=True)

    pesosOrden = []
    valoresOrden = []
    indicesOriginales = []
    for i in items:
        pesosOrden.append(i[0])
        valoresOrden.append(i[1])
        indicesOriginales.append(i[3]) 
    n = len(pesosOrden)

    # --- 2. Inicialización ---
    cola = ColaEncadenadaPrioridad()
    nodoInicial = Nodo(-1, 0, 0, 0, [])
    nodoInicial.setBound(calcularCota(nodoInicial, pesosOrden, valoresOrden, capacidad))
    cola.insertar(nodoInicial)

    maxValor = 0
    mejorSolucion = []

    # --- 3. Bucle principal: explorar nodos mientras haya en la cola ---
    while not cola.vacia():
        nodo = cola.suprimir()

        # Poda: no se explora si la cota no supera el mejor valor actual
        if nodo.getBound() >= maxValor and nodo.getNivel() < n-1:

            # --- 3.1 Generar hijo "con el siguiente objeto" ---
            nivelSig = nodo.getNivel() + 1
            pesoHijo = nodo.getPeso() + pesosOrden[nivelSig]
            valorHijo = nodo.getValor() + valoresOrden[nivelSig]
            elementosHijo = nodo.getElementos() + [nivelSig]

            hijoIncluido = Nodo(nivelSig, pesoHijo, valorHijo, 0, elementosHijo)
            hijoIncluido.setBound(calcularCota(hijoIncluido, pesosOrden, valoresOrden, capacidad))

            # Si el hijo es factible y mejora el valor actual, se actualiza la mejor solución
            if hijoIncluido.getPeso() <= capacidad and hijoIncluido.getValor() > maxValor:
                maxValor = hijoIncluido.getValor()
                mejorSolucion = hijoIncluido.getElementos()

            # Si el hijo tiene potencial, se inserta en la cola
            if hijoIncluido.getBound() > maxValor:
                cola.insertar(hijoIncluido)

            # --- 3.2 Generar hijo "sin el siguiente objeto" ---
            hijoExcluido = Nodo(nivelSig, nodo.getPeso(), nodo.getValor(), 0, nodo.getElementos())
            hijoExcluido.setBound(calcularCota(hijoExcluido, pesosOrden, valoresOrden, capacidad))

            # Solo se inserta si puede superar el valor actual
            if hijoExcluido.getBound() > maxValor:
                cola.insertar(hijoExcluido)

    # --- 4. Traducir índices al nombre original de las cajas ---
    cajas = []
    for i in mejorSolucion:
        letra = chr(65 + indicesOriginales[i])
        cajas.append(letra)

    return maxValor, cajas

if __name__ == '__main__':
    pesos = [2, 3, 5, 7, 9]
    valores = [10, 5, 15, 7, 20]
    capacidad = 15
    resultado, cajas = ramificacionYPoda(pesos, valores, capacidad)
    print("Valor máximo:", resultado)
    print("Cajas elegidas:", cajas)
