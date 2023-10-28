import math

def raiz_cuadrada(numero):
    if numero < 0:
        return "No se puede calcular la raíz cuadrada de un número negativo."
    else:
        return math.sqrt(numero)