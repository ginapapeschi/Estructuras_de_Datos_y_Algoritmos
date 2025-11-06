import numpy as np

class TablaHash:
    __tamaño: int
    __tabla: np.ndarray

    def __init__(self, tamaño):
        self.__tamaño = self.obtenerPrimo(round(tamaño/0.7)) # Ocupa el tamaño mayor para reducir la CARGA de la tabla (70% ocupada).
        self.__tabla = np.full(self.__tamaño, None, dtype=object) # Asegura que el tamaño final sea un NÚMERO PRIMO (para mejor dispersión de hashes). Se crea un arreglo lleno de None.

    def mostrarTabla(self):
        print(self.__tabla)

    def esPrimo(self, tamaño):
        esPrimo = True
        if tamaño < 2: # Los números menores a 2 no son primos.
            esPrimo = False
        else:
            i = 2
            while i <= int(tamaño ** 0.5) and esPrimo: # Itera desde 2 hasta la raíz cuadrada de tamaño. Si no hay divisores hasta la raíz de tamaño, no va a haber ninguno después.
                if tamaño % i == 0: # Se comprueba si tamaño es divisible entre 2 y su raíz.
                    esPrimo = False # Si encuentra un divisor, entonces no es primo.
                i += 1  
        return esPrimo

    def obtenerPrimo(self, tamaño): # Devuelve el número primo IGUAL o MAYOR al tamaño.
        if self.esPrimo(tamaño):
            resultado = tamaño # Si el tamaño ya es primo simplemente se retorna.
        else:
            siguiente = tamaño + 1 # Si no es primo se le suma uno y se pregunta hasta que esPrimo devuelva True.
            while not self.esPrimo(siguiente):
                siguiente += 1
            resultado = siguiente
        return resultado
    
    def hashing(self, valor:int): # Método de la división: índice = valor % tamaño de la tabla.
        return valor % self.__tamaño

    def metodoExtraccion(self, valor:int):
        valor = str(valor) # Convierte la clave a texto.
        valor = valor[-3:] # Toma los últimos 3 caracteres de la clave (extracción).
        return int(valor) % self.__tamaño # Convierte esos dígitos a número y aplica el método de la división.
        # índice = (clave extraída) % (tamaño de la tabla)
        # Sólo funciona bien si los últimos 3 dígitos varían bastante, de lo contrario se tendrán muchas colisiones.
    
    def metodoPlegado(self, valor:int):
        valor = str(valor) # Convierte el valor a texto para poder tomar fragmentos fácilmente.
        pares = []
        for i in range(0, len(valor), 2): # Va de 0 a la longitud de la cadena, tomando pares.
            pares.append(int(valor[i:i+2])) # Agrupa pares de strings: valor[inicio:fin], lo que quiere decir que dará todos los elementos desde la posición inicio hasta la posición fin (sin incluirlo). Esto toma dos elementos consecutivos, empezando en i.
            # Si el valor es 46407532, valor[i:i+2] PERMITE formar claves del tipo 46, 40, 75, 32. El for EVITA todas las posibles combinaciones de claves pares, tales como: 46, 64, 07, 75, 53, etc. Sólo salta de dos en dos.
        suma = sum(pares) # Suma todos los grupos.
        return suma % self.__tamaño # Aplica el método de la división.

    def metodoCuadradoMedio(self, valor:int): # Toma la clave, la eleva al cuadrado y luego extrae los dígitos del medio del resultado.
        valor = str(valor ** 2)
        medio = len(valor) // 2 # Calcula el índice del centro del número cuadrado.
        if len(valor) % 2 == 0: # Si el número de dígitos es par.
            grupo = valor[medio - 1 : medio + 1] # Toma dos del centro (desde medio-1 hasta medio+1, exlcuyendo al último, por lo que toma medio-1 y medio).
        else: # Si es impar.
            grupo = valor[medio - 1 : medio + 2] # Toma tres del centro (el del medio y uno a cada lado). El medio+2 es para que incluya a medio+1 también.
        return int(grupo) % self.__tamaño # Aplica el método de la división.

    def insertar(self, valor):
        indice = self.hashing(valor) # Calcula el índice inicial usando la función hashing(). Será el primer lugar donde se intentará insertar el valor.
        inicio = indice # Se guarda la posición inicial para saber cuándo se ha dado una vuelta completa a la tabla (lo que permite detectar si la tabla está llena).
        repetido = False # Indica si el valor ya existe en la tabla.
        tablaLlena = False
        colisiones = 0

        while self.__tabla[indice] is not None and not repetido and not tablaLlena:
            # Mientras la posición actual en la tabla esté OCUPADA, no se haya repetido un valor y no se haya recorrido toda la tabla se busca un lugar donde insertar el valor.
            if self.__tabla[indice] == valor: # Si el valor que se quiere insertar en la tabla ya existe (para evitar duplicados)
                repetido = True
            else: # Si el lugar está ocupado por otro valor hubo colisión.
                colisiones += 1
                print(f"Hubo colisión. Total de colisiones: {colisiones}")
                indice = (indice + 1) % self.__tamaño # SONDEO LINEAL - Se avanza una posición a la derecha, y % self.__tamaño hace que la tabla sea circular. Si se llega al final de la tabla, se vuelve al principio. 
                if indice == inicio: # Si depsués de moverse en la tabla se llegó al final, la tabla está llena.
                    tablaLlena = True

        if repetido:
            print("Valor no insertado, ya está en la tabla")
        elif tablaLlena:
            print("Tabla llena, no se pudo insertar")
        else: # Si no entró en el while en primera instancia implica que no hubo colisiones ni valores repetidos, por lo que se inserta directamente el valor en la tabla en el índice dado por la función hashing().
            self.__tabla[indice] = valor
            print(f"Valor insertado en la tabla")

    def buscar(self, valor):
        indice = self.hashing(valor) 
        inicio = indice
        encontrado = False
        tablaVacia = False
        
        while self.__tabla[indice] is not None and not encontrado and not tablaVacia: 
            # Mientras la posición actual tenga un valor, no se haya encontrado el valor y no se haya dado la vuelta a toda la tabla (no esté vacía).
            if self.__tabla[indice] == valor: # Se encontró el valor buscado.
                encontrado = True
            else:
                indice = (indice + 1) % self.__tamaño # SONDEO LINEAL - Se avanza a la siguiente posición.
            if indice == inicio:
                tablaVacia = True # Detiene la ejecución en caso de no encontrarse el valor en la tabla.
        
        return encontrado

if __name__ == '__main__':
    tabla = TablaHash(10)
    tabla.insertar(10)
    tabla.insertar(27)
    tabla.insertar(44)
    tabla.mostrarTabla()

    print(tabla.buscar(10))
    print(tabla.buscar(99))