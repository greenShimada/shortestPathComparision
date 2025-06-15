import ctypes
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
import matplotlib.pyplot as plt

MAX = 100
START = 0
GOAL = 1
MatrixType = (ctypes.c_int * MAX) * MAX

grafo_dll = ctypes.CDLL('../dll/grafo.dll')
dijkstra_dll = ctypes.CDLL('../dll/dijkstra.dll')
astar_dll = ctypes.CDLL('../dll/astar.dll')

grafo_dll.gerarGrafoAleatorio.argtypes = [ctypes.c_int, MatrixType]
grafo_dll.gerarGrafoAleatorio.restype = None

dijkstra_dll.dijkstra.argtypes = [ctypes.c_int, MatrixType, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
dijkstra_dll.dijkstra.restype = ctypes.c_int

astar_dll.astar.argtypes = [ctypes.c_int, MatrixType, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
astar_dll.astar.restype = ctypes.c_int

grafo = MatrixType()

d_count = 0
d_tempo = ctypes.c_double()
a_count = 0
a_tempo = ctypes.c_double()
empate = 0
a_total = 0
b_total = 0

iteracoes_totais = 100000

for i in range(iteracoes_totais):
    grafo_dll.gerarGrafoAleatorio(MAX, grafo)
    a = dijkstra_dll.dijkstra(MAX , grafo, START, GOAL, ctypes.byref(d_tempo))
    b = astar_dll.astar(MAX, grafo, START, GOAL, ctypes.byref(a_tempo))
    print(f"{a, b}")
    if a < b:
        d_count += 1
    elif a > b:
        a_count += 1
    else:
        empate += 1
    a_total += a 
    b_total += b



# Dados para os gráficos
tempos = [d_tempo.value / iteracoes_totais, a_tempo.value / iteracoes_totais]
custos = [a_total / iteracoes_totais, b_total / iteracoes_totais]
algoritmos = ['Dijkstra', 'A*']

# Cores suaves
cores = ['#888888', '#a8d5a2']  # cinza e verde claro

# Criar figura menor
plt.figure(figsize=(8, 4))

# Gráfico 1: Tempo médio por iteração
plt.subplot(1, 2, 1)
bars1 = plt.bar(algoritmos, tempos, color=cores)
plt.title('Tempo Médio')
plt.ylabel('Tempo (s)')
plt.grid(axis='y', linestyle='--', alpha=0.4)

# Adicionar labels acima das barras
for bar in bars1:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f"{yval:.6f}", 
             ha='center', va='bottom', fontsize=8)

# Gráfico 2: Custo médio do caminho
plt.subplot(1, 2, 2)
bars2 = plt.bar(algoritmos, custos, color=cores)
plt.title('Custo Médio do Caminho')
plt.ylabel('Custo')
plt.grid(axis='y', linestyle='--', alpha=0.4)

for bar in bars2:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f"{yval:.2f}", 
             ha='center', va='bottom', fontsize=8)

plt.tight_layout()
plt.show()

