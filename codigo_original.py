"""Códido que busca los números primos en un rango de 1 a 100,000"""
import time
import numpy as np

def primos_optimizado(limite):
    # Reducción del rango: solo hasta raíz cuadrada
    # Esto evita iterar innecesariamente y mejora tiempos.
    # Uso de arrays de NumPy: más eficiente que listas en operaciones vectorizadas.
    es_primo = np.ones(limite + 1, dtype=bool)  # inicializamos todo como True
    es_primo[:2] = False                        # 0 y 1 no son primos
    limite_raiz = int(np.sqrt(limite)) + 1      # calculamos raíz cuadrada del límite
    
    for i in range(2, limite_raiz):
        if es_primo[i]:
            #Marcado vectorizado: elimina múltiplos de i
            # Se usa slicing con paso "i" → mucho más rápido que bucles anidados.
            es_primo[i*i : limite+1 : i] = False   
    
    #List comprehension: extrae los índices que quedaron en True
    primos = [numero for numero in range(limite + 1) if es_primo[numero]]
    return primos

# Medición de tiempo.
inicio = time.time()
primos = primos_optimizado(100000)
fin = time.time()

# Resultados: cantidad de primos y tiempo de ejecución
print(f"Primos: {len(primos)}")
print(f"Tiempo optimizado: {fin - inicio:.4f} s")
