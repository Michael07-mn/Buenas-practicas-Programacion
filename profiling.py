import cProfile
import pstats
import numpy as np

def codigo_original(n):
    primos = []
    for i in range(2, n+1):
        es_primo = True
        for j in range(2, int(np.sqrt(i))+1):
            if i % j == 0:
                es_primo = False
                break
        if es_primo:
            primos.append(i)
    return primos

def primos_optimizado(limite):
    es_primo = np.ones(limite + 1, dtype=bool)
    es_primo[:2] = False
    limite_raiz = int(np.sqrt(limite)) + 1
    for i in range(2, limite_raiz):
        if es_primo[i]:
            es_primo[i*i : limite+1 : i] = False
    primos = [numero for numero in range(limite + 1) if es_primo[numero]]
    return primos

print("Perfilando código original...")
cProfile.run('codigo_original(10000)', 'profiling_original.prof')

print("Perfilando código optimizado...")
cProfile.run('primos_optimizado(10000)', 'profiling_optimizado.prof')

print("\n------ Estadísticas OPTIMIZADO ------")
stats = pstats.Stats('profiling_optimizado.prof')
stats.strip_dirs()
stats.sort_stats('time')
stats.print_stats(10)


with open("profiling_optimizado.txt", "w") as f:
    stats = pstats.Stats('profiling_optimizado.prof', stream=f)
    stats.strip_dirs()
    stats.sort_stats('time')
    stats.print_stats(10)
