#include "./headers/grafo.h"
#include <time.h>
#include <stdio.h>

DLL_EXPORT void gerarGrafoAleatorio(int G[MAX][MAX], int n) {
    static int seeded = 0;
    if (!seeded) {
        srand((unsigned int)(time(NULL)));
        seeded = 1;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i == j) {
                G[i][j] = 0; 
            } else {
                int aleatorio = rand() % 100;
                if (aleatorio < 30) {
                    G[i][j] = INFINITY; 
                } else {
                    G[i][j] = (rand() % 20) + 1000; 
                }
            }
        }
    }
}
