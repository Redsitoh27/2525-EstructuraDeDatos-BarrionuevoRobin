class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_inicio(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def tamaño(self):
        actual = self.cabeza
        contador = 0
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    def es_igual(self, otra_lista):
        actual1 = self.cabeza
        actual2 = otra_lista.cabeza

        while actual1 and actual2:
            if actual1.dato != actual2.dato:
                return False
            actual1 = actual1.siguiente
            actual2 = actual2.siguiente

        # Verifica que ambas terminen simultáneamente
        return actual1 is None and actual2 is None

# Uso del programa

def ejercicio9():
    n1 = int(input("Cantidad de datos para lista 1: "))
    lista1 = ListaEnlazada()
    print("Ingrese datos para lista 1:")
    for _ in range(n1):
        dato = int(input())
        lista1.agregar_inicio(dato)

    n2 = int(input("Cantidad de datos para lista 2: "))
    lista2 = ListaEnlazada()
    print("Ingrese datos para lista 2:")
    for _ in range(n2):
        dato = int(input())
        lista2.agregar_inicio(dato)

    tam1 = lista1.tamaño()
    tam2 = lista2.tamaño()

    if tam1 == tam2:
        if lista1.es_igual(lista2):
            print("a. Las listas son iguales en tamaño y contenido.")
        else:
            print("b. Las listas son iguales en tamaño pero no en contenido.")
    else:
        print("c. No tienen el mismo tamaño ni contenido.")

# Ejecutar
ejercicio9()
