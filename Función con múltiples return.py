def evaluar_numero(num):
    return "Positivo" if num > 0 else "Negativo" if num < 0 else "Cero"

# Llamada a la función:
print(evaluar_numero(10))  # Imprime: Positivo
print(evaluar_numero(-5))  # Imprime: Negativo
print(evaluar_numero(0))   # Imprime: Cero