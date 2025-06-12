#include "./headers/grafo.h"
#include <stdio.h>


DLL_EXPORT int dijkstra(int cost[MAX][MAX], int n, int startnode, int goal, double* tempo_execucao) {
    clock_t inicio = clock();

    int distance[MAX], pred[MAX];
    int visited[MAX], mindistance, nextnode, i, j;

    for (i = 0; i < n; i++) {
        distance[i] = cost[startnode][i];
        pred[i] = startnode;
        visited[i] = 0;
    }

    distance[startnode] = 0;
    visited[startnode] = 1;

    while (1) {
        mindistance = INFINITY;
        nextnode = -1;

        for (i = 0; i < n; i++) {
            if (distance[i] < mindistance && !visited[i]) {
                mindistance = distance[i];
                nextnode = i;
            }
        }

        if (nextnode == -1 || nextnode == goal)
            break;

        visited[nextnode] = 1;

        for (i = 0; i < n; i++) {
            if (!visited[i] && cost[nextnode][i] != -1) {
                int newdist = distance[nextnode] + cost[nextnode][i];
                if (newdist < distance[i]) {
                    distance[i] = newdist;
                    pred[i] = nextnode;
                }
            }
        }
    }

    clock_t fim = clock();
    if (tempo_execucao != NULL) {
        *tempo_execucao += (double)(fim - inicio) / CLOCKS_PER_SEC;
    }
    
    return distance[goal];
}