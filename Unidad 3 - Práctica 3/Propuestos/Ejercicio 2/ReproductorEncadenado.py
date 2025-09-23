class Cancion:
    __nombre: str
    __sig: int

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__sig = None

    def getNombre(self):
        return self.__nombre
    
    def getSiguiente(self):
        return self.__sig
    
    def setSiguiente(self, siguiente):
        self.__sig = siguiente
    
class ListaEncadenada:
    __cabeza: Cancion
    __cant: int

    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    
    def vacia(self):
        return self.__cant == 0
    
    def buscar(self, nombre):
        actual = self.__cabeza
        while actual != None:
            if actual.getNombre().lower() == nombre.lower():
                return actual
            actual = actual.getSiguiente()
        return None
    
    def mostrarTituloPorPos(self, pos):
        if 0 <= pos < self.__cant:
            if pos == 0:
                actual = self.__cabeza
            else:
                actual = self.__cabeza
                for i in range(pos):
                    actual = actual.getSiguiente()

            print(f"La canción en la posición {pos} es: '{actual.getNombre()}'")

        else:
            print("Posición fuera de rango")

    def buscarPorNombre(self, nombre):
        actual = self.__cabeza
        pos = 0
        while actual != None:
            if actual.getNombre().lower() == nombre.lower():
                return pos
            pos += 1
            actual = actual.getSiguiente()
        return -1
    
    def mostrarPosPorTitulo(self, nombre):
        pos = self.buscarPorNombre(nombre)
        if pos != -1:
            print(f"La canción se encuentra almacenada en la posición {pos}")
        else:
            print(f"La canción no se encontró")

    def insertarAlFinal(self, nombre):
        if self.buscar(nombre):
            print("La canción ingresada ya existe")
        else:
            nuevo = Cancion(nombre)
            if self.vacia():
                self.__cabeza = nuevo
                print(f"Canción '{nombre}' agregada al inicio del reproductor")
            else:
                actual = self.__cabeza
                while actual.getSiguiente() != None:
                    actual = actual.getSiguiente()
                actual.setSiguiente(nuevo)
                print(f"Canción '{nombre}' agregada al final del reproductor")
            self.__cant += 1

    def insertarPorPosicion(self, pos, nombre):
        if 0 <= pos <= self.__cant:
            if self.buscar(nombre):
                print("La canción ingresada ya existe")
            
            else:
                nuevo = Cancion(nombre)
                if pos == 0:
                    nuevo.setSiguiente(self.__cabeza)
                    self.__cabeza = nuevo

                else:
                    actual = self.__cabeza
                    for i in range(pos - 1):
                        actual = actual.getSiguiente()
                    nuevo.setSiguiente(actual.getSiguiente())
                    actual.setSiguiente(nuevo)

                self.__cant += 1
                print(f"Canción '{nombre}' agregada en la posición {pos}")
                
        else: print("Posición fuera de rango")

    def suprimirPorPos(self, pos):
        if 0 <= pos < self.__cant:
            if not self.vacia():
                if pos == 0:
                    eliminado = self.__cabeza.getNombre()
                    self.__cabeza = self.__cabeza.getSiguiente()
                else:
                    anterior = None
                    actual = self.__cabeza
                    for i in range(pos):
                        anterior = actual
                        actual = anterior.getSiguiente()
                    eliminado = actual.getNombre()
                    anterior.setSiguiente(actual.getSiguiente())
                
                self.__cant -= 1
                print(f"Canción eliminada de la posición {pos}: {eliminado}")
            
            else: print("Lista vacía")
        else: print("Posición fuera de rango")

    def mostrar(self):
        i = 0
        actual = self.__cabeza
        print(f"Canciones del reproductor:")
        while actual != None:
            print(f"[{i}] -> {actual.getNombre()}")
            actual = actual.getSiguiente()
            i += 1

def menu():
    print()
    print("MENÚ DE OPCIONES".center(70))
    op = input('''
a) Agregar una canción al final de la lista
b) Agregar una canción en una posición específica
c) Mostrar el título de una canción
d) Mostrar posición en la que se almacena una canción
e) Eliminar canción
f) Mostrar lista de reproducción                              
z) SALIR               
Su opción -> ''')
    return op

if __name__ == '__main__':
    lista = ListaEncadenada()
    lista.insertarAlFinal('A')
    lista.insertarAlFinal('B')
    lista.insertarAlFinal('C')
    lista.mostrarTituloPorPos(2)
    opcion = menu().lower()

    while opcion != 'z':
        if opcion == 'a':
            nombre = input("\nIngrese el nombre: ")
            lista.insertarAlFinal(nombre)
        
        elif opcion == 'b':
            nombre = input("\nIngrese el nombre: ")
            posicion = int(input("Ingrese la posición: "))
            lista.insertarPorPosicion(posicion, nombre)
        
        elif opcion == 'c':
            posicion = int(input("Ingrese la posición: "))
            lista.mostrarTituloPorPos(posicion)

        elif opcion == 'd':
            nombre = input("\nIngrese el nombre: ")
            lista.mostrarPosPorTitulo(nombre)
        
        elif opcion == 'e':
            posicion = int(input("\nIngrese la posición: "))
            lista.suprimirPorPos(posicion)

        elif opcion == 'f':
            lista.mostrar()

        else: print("\nOpción inválida")
    
        opcion = menu().lower()