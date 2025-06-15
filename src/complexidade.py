import ctypes
import numpy as np
import matplotlib.pyplot as plt

grafo_dll = ctypes.CDLL('../dll/grafo.dll')
dijkstra_dll = ctypes.CDLL('../dll/dijkstra.dll')
astar_dll = ctypes.CDLL('../dll/astar.dll')

# sera feita 100 iteracoes para cada valor de matriz - 100x100, 200x200 até 2000x2000
iteracoes_por_teste = 100
max_values = list(range(100, 2100, 100)) 
START = 0
GOAL = 1

tempo_astar = []
tempo_dijkstra = []

for n in max_values:
    print(f"Testando com {n} nós...")

    MatrixType = (ctypes.c_int * n) * n
    grafo = MatrixType()

    grafo_dll.gerarGrafoAleatorio.argtypes = [ctypes.c_int, MatrixType]
    dijkstra_dll.dijkstra.argtypes = [ctypes.c_int, MatrixType, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]
    astar_dll.astar.argtypes = [ctypes.c_int, MatrixType, ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_double)]

    total_tempo_astar = 0.0
    total_tempo_dijkstra = 0.0

    for _ in range(iteracoes_por_teste):
        grafo_dll.gerarGrafoAleatorio(n, grafo)

        t_astar = ctypes.c_double(0)
        t_dijkstra = ctypes.c_double(0)

        astar_dll.astar(n, grafo, START, GOAL, ctypes.byref(t_astar))
        dijkstra_dll.dijkstra(n, grafo, START, GOAL, ctypes.byref(t_dijkstra))

        total_tempo_astar += t_astar.value
        total_tempo_dijkstra += t_dijkstra.value
        
    print(f"Tempo para matrix {n}x{n} = D{total_tempo_dijkstra / iteracoes_por_teste} - A{total_tempo_astar / iteracoes_por_teste}")
    tempo_astar.append(total_tempo_astar / iteracoes_por_teste)
    tempo_dijkstra.append(total_tempo_dijkstra / iteracoes_por_teste)


fit_astar = np.polyfit(max_values, tempo_astar, deg=2)
fit_dijkstra = np.polyfit(max_values, tempo_dijkstra, deg=2)

plt.figure(figsize=(9, 5))
plt.plot(max_values, tempo_astar, label='A*', marker='o', color='#7FB77E')
plt.plot(max_values, tempo_dijkstra, label='Dijkstra', marker='o', color='#555555')

# CURVAS DE AJUSTE OTIMO
x_fit = np.linspace(100, 2000, 500)
plt.plot(x_fit, np.polyval(fit_astar, x_fit), '--', color='#7FB77E', alpha=0.5)
plt.plot(x_fit, np.polyval(fit_dijkstra, x_fit), '--', color='#555555', alpha=0.5)

plt.title('Tempo Médio vs Número de Nós (Complexidade)')
plt.xlabel('Número de Nós (n)')
plt.ylabel('Tempo Médio (s)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
