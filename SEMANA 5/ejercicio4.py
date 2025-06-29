class Loteria:
    def __init__(self):
        self.numeros = []

    def ingresar_numeros(self):
        entrada = input("Ingrese los números ganadores separados por comas: ")
        self.numeros = sorted([int(x.strip()) for x in entrada.split(",")])

    def mostrar_numeros(self):
        print("Números ganadores ordenados:", self.numeros)

loteria = Loteria()
loteria.ingresar_numeros()
loteria.mostrar_numeros()
