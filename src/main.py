import ctypes
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

MAX = 100
START = 0
GOAL = 68
MatrixType = (ctypes.c_int * MAX) * MAX

grafo_dll = ctypes.CDLL('../dll/grafo.dll')
dijkstra_dll = ctypes.CDLL('../dll/dijkstra.dll')
astar_dll = ctypes.CDLL('../dll/astar.dll')

grafo_dll.gerarGrafoAleatorio.argtypes = [MatrixType, ctypes.c_int]
grafo_dll.gerarGrafoAleatorio.restype = None

dijkstra_dll.dijkstra.argtypes = [MatrixType, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
dijkstra_dll.dijkstra.restype = ctypes.c_int

astar_dll.astar.argtypes = [MatrixType, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
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
    grafo_dll.gerarGrafoAleatorio(grafo, MAX)
    a = dijkstra_dll.dijkstra(grafo, MAX, START, GOAL, ctypes.byref(d_tempo))
    b = astar_dll.astar(grafo, MAX, START, GOAL, ctypes.byref(a_tempo))
    print(f"{a, b}")
    if a < b:
        d_count += 1
    elif a > b:
        a_count += 1
    else:
        empate += 1
    a_total += a 
    b_total += b

print("\n\t--- RESULTADOS ---")
print(f"Total de execuções         : {iteracoes_totais}")
print(f"Vitórias do Dijkstra       : {d_count}")
print(f"Vitórias do A*             : {a_count}")
print(f"Empates                    : {empate}")
print(f"\nTempo total do Dijkstra    : {d_tempo.value:.6f} segundos")
print(f"Tempo total do A*          : {a_tempo.value:.6f} segundos")

# Cálculo de tempo médio
if d_count + a_count + empate > 0:
    print(f"\n\t------- Médias ---------:")
    print(f" - Dijkstra                : {d_tempo.value / iteracoes_totais:.8f} s por iteração")
    print(f" - A*                      : {a_tempo.value / iteracoes_totais:.8f} s por iteração")
    print(f" - Dijkstra                : {a_total / iteracoes_totais:.3f} (média de custo de caminho)")
    print(f" - A*                      : {b_total / iteracoes_totais:.3f} (média de custo de caminho)")

dif_tempo = d_tempo.value - a_tempo.value
dif_custo = (b_total - a_total)

percent_tempo = abs(dif_tempo) / max(d_tempo.value, a_tempo.value) * 100 if max(d_tempo.value, a_tempo.value) > 0 else 0
percent_custo = abs(dif_custo) / max(a_total, b_total) * 100 if max(a_total, b_total) > 0 else 0

mais_rapido = "A*" if a_tempo.value < d_tempo.value else "Dijkstra"
mais_longo = "A*" if a_total < b_total else "Dijkstra"

print(f"\nConclusão:")
print(f"{mais_rapido} é aproximadamente {percent_tempo:.2f}% mais rápido, "
      f"porém encontra caminhos aproximadamente {percent_custo:.2f}% mais {'longos' if mais_longo == 'A*' else 'curtos'}.")
