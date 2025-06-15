#include "./headers/grafo.h"

int x[MAX], y[MAX]; 

typedef struct {
    int node;
    int f_score; 
} PQNode;

typedef struct {
    PQNode data[MAX];
    int size;
} PriorityQueue;

void swap(PQNode *a, PQNode *b) {
    PQNode temp = *a;
    *a = *b;
    *b = temp;
}

void push(PriorityQueue *pq, int node, int f_score) {
    int i = pq->size++;
    pq->data[i].node = node;
    pq->data[i].f_score = f_score;

    while (i > 0 && pq->data[i].f_score < pq->data[(i - 1) / 2].f_score) {
        swap(&pq->data[i], &pq->data[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}

int pop(PriorityQueue *pq) {
    if (pq->size == 0) return -1;
    int node = pq->data[0].node;
    pq->data[0] = pq->data[--pq->size];

    int i = 0;
    while (1) {
        int smallest = i;
        int left = 2*i + 1, right = 2*i + 2;
        if (left < pq->size && pq->data[left].f_score < pq->data[smallest].f_score)
            smallest = left;
        if (right < pq->size && pq->data[right].f_score < pq->data[smallest].f_score)
            smallest = right;
        if (smallest == i) break;
        swap(&pq->data[i], &pq->data[smallest]);
        i = smallest;
    }

    return node;
}

int heuristic(int a, int b) {
    return 1000;
}

DLL_EXPORT int astar(int cost[MAX][MAX], int n, int startnode, int goal, double* tempo_execucao) {
    clock_t inicio = clock();

    int g_score[MAX], f_score[MAX], pred[MAX], visited[MAX] = {0};
    PriorityQueue pq = { .size = 0 };

    for (int i = 0; i < n; i++) {
        g_score[i] = INFINITY;
        f_score[i] = INFINITY;
        pred[i] = -1;
    }

    g_score[startnode] = 0;
    f_score[startnode] = heuristic(startnode, goal);
    push(&pq, startnode, f_score[startnode]);

    while (pq.size > 0) {
        int current = pop(&pq);

        if (current == goal)
            break;

        if (visited[current])
            continue;

        visited[current] = 1;

        for (int neighbor = 0; neighbor < n; neighbor++) {
            if (cost[current][neighbor] != -1) {
                int tentative_g = g_score[current] + cost[current][neighbor];
                if (tentative_g < g_score[neighbor]) {
                    g_score[neighbor] = tentative_g;
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal);
                    pred[neighbor] = current;
                    push(&pq, neighbor, f_score[neighbor]);
                }
            }
        }
    }

    clock_t fim = clock();
    if (tempo_execucao != NULL) {
        *tempo_execucao += (double)(fim - inicio) / CLOCKS_PER_SEC;
    }

    return g_score[goal];
}

