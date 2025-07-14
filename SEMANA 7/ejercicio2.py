def mover_disco(origen, destino, torres):
    """
    Mueve el disco superior de la pila de origen a la pila de destino.

    Parámetros:
    origen (str): nombre de la torre origen.
    destino (str): nombre de la torre destino.
    torres (dict): diccionario con las pilas de cada torre.
    """
    disco = torres[origen].pop()
    torres[destino].append(disco)
    print(f"Mover disco {disco} de {origen} a {destino}")

def hanoi(n, origen, auxiliar, destino, torres):
    """
    Soluciona el problema de las Torres de Hanoi usando recursión y pilas.

    Parámetros:
    n (int): número de discos.
    origen (str): torre origen.
    auxiliar (str): torre auxiliar.
    destino (str): torre destino.
    torres (dict): diccionario con las pilas de cada torre.
    """
    if n == 1:
        mover_disco(origen, destino, torres)
    else:
        hanoi(n-1, origen, destino, auxiliar, torres)
        mover_disco(origen, destino, torres)
        hanoi(n-1, auxiliar, origen, destino, torres)

# Inicialización de las torres como pilas
def ejecutar_hanoi(num_discos):
    """
    Prepara y ejecuta la resolución de las Torres de Hanoi.

    Parámetros:
    num_discos (int): número de discos en la torre inicial.
    """
    torres = {
        'A': list(reversed(range(1, num_discos + 1))),  # Torre origen con discos
        'B': [],  # Torre auxiliar
        'C': []   # Torre destino
    }

    print(f"\n--- Resolviendo Torres de Hanoi con {num_discos} discos ---")
    hanoi(num_discos, 'A', 'B', 'C', torres)

# Ejemplo de ejecución con 3 discos
ejecutar_hanoi(3)
