class Palindromo:
    def __init__(self, palabra):
        self.palabra = palabra

    def es_palindromo(self):
        return self.palabra.lower() == self.palabra[::-1].lower()

    def mostrar_resultado(self):
        if self.es_palindromo():
            print(f"La palabra '{self.palabra}' es un palíndromo.")
        else:
            print(f"La palabra '{self.palabra}' no es un palíndromo.")

palabra_usuario = input("Introduce una palabra: ")
verificador = Palindromo(palabra_usuario)
verificador.mostrar_resultado()