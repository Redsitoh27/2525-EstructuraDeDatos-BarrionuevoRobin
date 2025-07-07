class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_final(self, dato):
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        datos = []
        while actual:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos

    def promedio(self):
        actual = self.cabeza
        suma = 0
        contador = 0
        while actual:
            suma += actual.dato
            contador += 1
            actual = actual.siguiente
        return suma / contador if contador > 0 else 0

    def separar_por_promedio(self, promedio):
        lista_menor_igual = ListaEnlazada()
        lista_mayor = ListaEnlazada()

        actual = self.cabeza
        while actual:
            if actual.dato <= promedio:
                lista_menor_igual.agregar_final(actual.dato)
            else:
                lista_mayor.agregar_final(actual.dato)
            actual = actual.siguiente

        return lista_menor_igual, lista_mayor

# Uso del programa

def ejercicio8():
    n = int(input("Cantidad de datos reales: "))
    lista_principal = ListaEnlazada()

    for _ in range(n):
        dato = float(input("Ingrese dato real: "))
        lista_principal.agregar_final(dato)

    print("\nDatos en lista principal:", lista_principal.mostrar())

    prom = lista_principal.promedio()
    print("Promedio:", prom)

    lista_menor_igual, lista_mayor = lista_principal.separar_por_promedio(prom)

    print("Datos <= promedio:", lista_menor_igual.mostrar())
    print("Datos > promedio:", lista_mayor.mostrar())

# Ejecutar
ejercicio8()
