# graficos.py
import matplotlib.pyplot as plt
import numpy as np
import time
from codigo_original import es_primo as es_primo_orig
from codigo_optimizado import es_primo_optimizado

# Medir tiempos para varios tamaños (opcional: desde 10k hasta 100k)
tamanios = [20000, 40000, 60000, 80000, 100000]
tiempos_orig = []
tiempos_opt = []

for N in tamanios:
    # Tiempo original
    inicio = time.time()
    primos_orig = [num for num in range(1, N+1) if es_primo_orig(num)]
    tiempos_orig.append(time.time() - inicio)
    
    # Tiempo optimizado
    inicio = time.time()
    primos_opt = es_primo_optimizado(N)
    tiempos_opt.append(time.time() - inicio)

# Gráfico comparativo
plt.figure(figsize=(10, 5))
plt.plot(tamanios, tiempos_orig, 'o-', label='Código original', color='red')
plt.plot(tamanios, tiempos_opt, 's-', label='Código optimizado', color='green')
plt.xlabel('Límite superior (N)')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos: Original vs Optimizado')
plt.legend()
plt.grid(True)
plt.savefig('comparacion_tiempos.png')
plt.show()
plt.close()

# Gráfico de barras para 100,000
plt.figure(figsize=(7, 5))
categorias = ['Original', 'Optimizado']
tiempos_finales = [tiempos_orig[-1], tiempos_opt[-1]]
plt.bar(categorias, tiempos_finales, color=['gray', 'purple'])
plt.ylabel('Tiempo (segundos)')
plt.title('Tiempo para N = 100,000')
for i, v in enumerate(tiempos_finales):
    plt.text(i, v + 0.5, f"{v:.3f}s", ha='center')
plt.savefig('barra_comparativa.png')
plt.show()
plt.close()
