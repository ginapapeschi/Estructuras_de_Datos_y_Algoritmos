class Contacto:
    __nombre: str
    __telefono: str
    __sig: int

    def __init__(self, nombre, telefono):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__sig = None

    def getNombre(self):
        return self.__nombre
    
    def getTelefono(self):
        return self.__telefono

    def getSiguiente(self):
        return self.__sig
    
    def setSiguiente(self, siguiente):
        self.__sig = siguiente

class ListaEncadenada:
    __cabeza: Contacto
    __cant: int

    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, nombre, telefono):
        if self.buscar(nombre):
            print("Contacto ya agendado")
        else:
            nuevo = Contacto(nombre, telefono)
            if self.__cant:
                anterior = None
                actual = self.__cabeza
                while actual != None and actual.getNombre().lower() < nombre.lower():
                    anterior = actual
                    actual = actual.getSiguiente()

                if anterior:
                    nuevo.setSiguiente(anterior.getSiguiente())
                    anterior.setSiguiente(nuevo)

                else:
                    nuevo.setSiguiente(self.__cabeza)
                    self.__cabeza = nuevo

            else:
                self.__cabeza = nuevo

            self.__cant += 1
            print(f"Contacto {nombre} - Tel: {telefono} agendado")

    def suprimir(self, nombre):
        if self.buscar(nombre):
            if not self.vacia():
                anterior = None
                actual = self.__cabeza
                eliminado = actual
                while actual != None and actual.getNombre().lower() != nombre.lower():
                    anterior = actual
                    actual = anterior.getSiguiente()
                if anterior:
                    eliminado = actual
                    anterior.setSiguiente(actual.getSiguiente())
                else:
                    self.__cabeza = actual.getSiguiente()
                self.__cant -= 1
                print(f"Contacto eliminado: {eliminado.getNombre()} - Teléfono: {eliminado.getTelefono()}")
            else:
                print("Lista vacía")
        else:
            print("Contacto no encontrado")

    def recorrer(self):
        i = 0
        actual = self.__cabeza
        print("\nLista de contactos:")
        while actual != None:
            print(f"[{i}] -> {actual.getNombre()} - Teléfono {actual.getTelefono()}")
            actual = actual.getSiguiente()
            i += 1
    
    def buscar(self, nombre):
        actual = self.__cabeza
        while actual != None:
            if actual.getNombre().lower() == nombre.lower():
                return actual
            actual = actual.getSiguiente()
        return None
    
    def mostrarTelefono(self, nombre):
        contacto = self.buscar(nombre)
        if contacto:
            print(f"Número de teléfono de {nombre}: {contacto.getTelefono()}")
        else:
            print("Contacto no agendado")

def menu():
    print()
    print("MENÚ DE OPCIONES".center(70))
    op = input('''
a) Agregar contacto
b) Eliminar contacto
c) Buscar contacto
d) Listar contactos
z) SALIR               
Su opción -> ''')
    return op

if __name__ == '__main__':
    lista = ListaEncadenada()
    opcion = menu().lower()

    while opcion != 'z':
        if opcion == 'a':
            nombre = input("\nIngrese el nombre: ")
            telefono = input("Ingrese el teléfono: ")
            lista.insertar(nombre, telefono)
        
        elif opcion == 'b':
            nombre = input("\nIngrese el nombre: ")
            lista.suprimir(nombre)
        
        elif opcion == 'c':
            nombre = input("\nIngrese el nombre: ")
            lista.mostrarTelefono(nombre)

        elif opcion == 'd':
            lista.recorrer()

        else: print("\nOpción inválida")
    
        opcion = menu().lower()

'''
LOTE DE PRUEBA
a
Maria Fernandez
2644564567
a
Mario Hugo
2645482049
a
Andrea Perez
2641231234
a
Andres Quiroga
2645678768
a
Zoe Martinez
2648908764
d
c
Maria Fernandez
b
Mario Hugo
d
'''