
#ifndef GRAFO_H
#define GRAFO_H

#define INFINITY 9999

#ifdef _WIN32
  #define DLL_EXPORT __declspec(dllexport)
#else
  #define DLL_EXPORT
#endif

#include <stdlib.h>
#include <stdio.h>
#include <time.h>

DLL_EXPORT void gerarGrafoAleatorio(int n, int G[n][n]);
DLL_EXPORT int astar(int n, int cost[n][n], int startnode, int goal, double* tempo_execucao);
DLL_EXPORT int dijkstra(int n, int cost[n][n], int startnode, int goal, double* tempo_execucao); 

#endif
