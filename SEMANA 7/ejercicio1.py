def esta_balanceada(expresion):
    """
    Verifica si una expresión matemática tiene los símbolos {}, [], () balanceados.

    Parámetros:
    expresion (str): cadena con la expresión a verificar.

    Retorna:
    bool: True si está balanceada, False en caso contrario.
    """
    pila = []
    pares = {')': '(', ']': '[', '}': '{'}

    for caracter in expresion:
        if caracter in '([{':
            pila.append(caracter)  # Se apila símbolo de apertura
        elif caracter in ')]}':
            if not pila or pila[-1] != pares[caracter]:
                return False  # No hay símbolo de apertura correspondiente
            pila.pop()  # Se desapila el símbolo correcto

    return len(pila) == 0  # Si la pila está vacía, está balanceada


# Ejemplo de uso
expresion = "{7 + (8 * 5) - [(9 - 7) + (4 + 1)]}"
if esta_balanceada(expresion):
    print("Fórmula balanceada.")
else:
    print("Fórmula NO balanceada.")
