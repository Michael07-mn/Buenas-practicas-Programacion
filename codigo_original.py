"""Códido que busca los números primos en un rango de 1 a 100,000"""
import time

# Crear una funcion que defina si es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

inicio = time.time()
primos = [num for num in range(1, 100001) if es_primo(num)]
fin = time.time()

print(f"Cantidad de números primos encontrados: {len(primos)}")
print(f"Tiempo de ejecución: {fin - inicio:.5f} segundos.")

