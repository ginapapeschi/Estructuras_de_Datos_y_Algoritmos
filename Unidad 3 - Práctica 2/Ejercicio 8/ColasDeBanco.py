from random import random, choice, expovariate

class Cliente:
    __tiempoLlegada: int # Minuto en que el cliente llegó al banco.
    __sig: int

    def __init__(self, tiempo):
        self.__tiempoLlegada = tiempo
        self.__sig = None

    def getTiempoLlegada(self):
        return self.__tiempoLlegada
    
    def setTiempoLlegada(self, tiempo):
        self.__tiempoLlegada = tiempo

    def getSiguiente(self):
        return self.__sig
    
    def setSiguiente(self, siguiente):
        self.__sig = siguiente

class ColaEncadenada:
    __primero: Cliente
    __ultimo: Cliente
    __cant: int

    def __init__(self):
        self.__primero = None
        self.__ultimo = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0
    
    def recuperar(self): # Devuelve el cliente al frente de la cola sin eliminarlo.
        return self.__primero 
    
    def insertar(self, tiempo):
        nuevo = Cliente(tiempo)

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
            tiempo = self.__primero.getTiempoLlegada()
            self.__primero = self.__primero.getSiguiente()
            self.__cant -= 1

            if self.__primero is None:
                self.__ultimo = None
            
            return tiempo
        
    def recorrer(self):
        if not self.vacia():
            print("\nElementos de la cola:")
            actual = self.__primero
            i = 0
            while actual != None:
                print(f"[{i}] -> {actual.getTiempoLlegada()}")
                actual = actual.getSiguiente()
                i += 1
        
        else:
            print("Cola vacía")

    def getCantidadClientes(self):
        return self.__cant

# Funciones auxiliares.
def getCajerosLibres(colas): # Devuelve una lista de índices de cajeros libres (colas vacías).
    cajerosLibres = []
    for i, cola in enumerate(colas): # Recorre cada elemento de la lista de colas y además le asigna un índice automáticamente (i).
        if cola.vacia():
            cajerosLibres.append(i)
    return cajerosLibres

def colaConMenosClientes(colas): # Devuelve los índices de la/s cola/s con menos clientes.
    min = 1000
    eleccion = []
    for i, cola in enumerate(colas):
        if cola.getCantidadClientes() < min:
            min = cola.getCantidadClientes()
            eleccion = [i]
        elif cola.getCantidadClientes() == min:
            eleccion.append(i)
    return eleccion # Si hay empate, devuelve todos los índices empatados. Como pueden ser más de uno, devuelve una lista.

def inicializarTiempoCajero(indice): # Inicializa el tiempo de atención de cada cajero según el índice.
    if indice == 0: # Cajero 1: 5 minutos fijos.
        tiempo = 5
    elif indice == 1: # Cajero 2: 3 minutos fijos.
        tiempo = 3
    elif indice == 2: # Cajero 3: promedio de 4 minutos, mínimo 1.
        tiempo = max(1, round(expovariate(1/4))) # Número aleatorio con media 4
        # Expovariate genera un número aleatorio con distribución exponencial. La media es de 4 minutos (definición de media es 1/λ, se calcula con expovariate). Puede dar 0.3, 7.2, 4.8, etc.
        # Se redondea el número aleatorio al entero más cercano, y max garantiza que el tiempo nunca sea menor a 1 (como en casos de round(0.2)).

    return tiempo

if __name__ == '__main__':
    cola1 = ColaEncadenada()
    cola2 = ColaEncadenada()
    cola3 = ColaEncadenada()
    colas = [cola1, cola2, cola3] # Se crean las 3 colas independientes y se guardan en una lista.

    tiempoSimulacion = 120 # Simulación de 2 horas.
    reloj = 0 # Tiempo actual de la simulación, minuto a minuto.
    tiempoEspera = 0 # Se usa cuando el cliente es atendido para calcular cuánto esperó desde que llegó hasta ser atendido.
    tiempoTotalAtencion = 0 # Suma todos los tiempos de espera de los clientes atendidos.
    tiemposRestantes = [0, 0, 0] # Lista de los tiempos de cada cajero, cuánto le falta para terminar con su cliente actual. 0 significa que el cajero está libre.
    clientesAtendidos = 0
    tiempoMaximoEspera = 0 # Tiempo máximo que un cliente ha esperado en la cola durante toda la simulación. Se actualiza cada vez que un cliente termina de ser atendido y su tiempo de espera supera el valor actual.

    while reloj < tiempoSimulacion:
        for i in range(3):
            if tiemposRestantes[i] > 0: # Si el cajero está ocupado, se resta un minuto.
                tiemposRestantes[i] -= 1
            elif not colas[i].vacia(): # Si el cajero está libre y hay clientes, atiende al primero de la cola.
                tiempoLlegada = colas[i].suprimir() # Se saca el cliente cuando el contador llegó a 0, guardando el tiempo de llegada.
                tiemposRestantes[i] = inicializarTiempoCajero(i) # Se inicializa el tiempo de espera del cajero correspondiente.
                tiempoEspera = reloj - tiempoLlegada 
                tiempoTotalAtencion += tiempoEspera # Suma el total y aumenta el contador de clientes atendidos.
                clientesAtendidos += 1

                if tiempoEspera >= tiempoMaximoEspera:
                    tiempoMaximoEspera = tiempoEspera # Se calcula el máximo esperado.

        if random() <= 0.5: # Simula la llegada de un cliente. Por minuto hay un 50% de probabilidad de que llegue un cliente.
            # Se decide a qué cola el cliente irá:
            cajerosLibres = getCajerosLibres(colas)
            if cajerosLibres:
                indice = choice(cajerosLibres) # Si todos los cajeros están libres, se elige al azar.
            else: # Si todos los cajeros están ocupados, se elige entre ellos la cola más corta.
                indice = choice(colaConMenosClientes(colas)) # Si hay la misma cantidad en más de una cola, la elección es aleatoria.
        
            # Una vez elegida la cola:
            colas[indice].insertar(reloj) # Inserta el cliente en la cola correspondiente (con el índice) el tiempo de llegada del cliente.

            if tiemposRestantes[indice] == 0: # Si el cajero está libre.
                tiemposRestantes[indice] = inicializarTiempoCajero(indice) # Inicializa su tiempo de atención para que lo atienda inmediatamente.
        
        reloj += 1 # Avanza un minuto en la simulación.

    totalEsperaSinAtender = 0 # Seguir explicando ---
    cantidadSinAtender = 0

    for cola in colas:
        cantidadSinAtender += cola.getCantidadClientes()
        while not cola.vacia():
            tiempoLlegada = cola.suprimir()
            totalEsperaSinAtender += tiempoSimulacion - tiempoLlegada

    print(f"Tiempo máximo de espera: {tiempoMaximoEspera} minutos")
    print(f"Cantidad de clientes atendidos: {clientesAtendidos}")
    print(f"Cantidad de clientes sin atender: {cantidadSinAtender}")
    if clientesAtendidos > 0:
        print(f"Promedio de espera de los clientes atendidos: {tiempoTotalAtencion / clientesAtendidos:.2f} minutos")
    if cantidadSinAtender > 0:
        print(f"Promedio de espera de los clientes sin atender: {totalEsperaSinAtender / cantidadSinAtender:.2f} minutos")
