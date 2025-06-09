import math

# Clase Circulo que encapsula el radio
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Clase Rectangulo que encapsula base y altura
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

def main():
    print("=== Cálculo para un Círculo ===")
    radio = float(input("Ingrese el radio del círculo: "))
    circulo = Circulo(radio)
    print(f"Área del círculo: {circulo.calcular_area():.2f}")
    print(f"Perímetro del círculo: {circulo.calcular_perimetro():.2f}")

    print("\n=== Cálculo para un Rectángulo ===")
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    rectangulo = Rectangulo(base, altura)
    print(f"Área del rectángulo: {rectangulo.calcular_area():.2f}")
    print(f"Perímetro del rectángulo: {rectangulo.calcular_perimetro():.2f}")

if __name__ == "__main__":
    main()

