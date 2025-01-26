#include <stdio.h>
#include <stdbool.h>

#define MAX 10 // Maximum number of vertices in the graph

// Function prototypes
void DFS(int graph[MAX][MAX], int visited[MAX], int vertex, int numVertices);

int main() {
    int graph[MAX][MAX];
    int visited[MAX] = {0}; // Keeps track of visited vertices
    int numVertices, startVertex;

    // Input the number of vertices
    printf("Enter the number of vertices in the graph: ");
    scanf("%d", &numVertices);

    // Input the adjacency matrix
    printf("Enter the adjacency matrix of the graph:\n");
    for (int i = 0; i < numVertices; i++) {
        for (int j = 0; j < numVertices; j++) {
            scanf("%d", &graph[i][j]);
        }
    }

    // Input the starting vertex for DFS
    printf("Enter the starting vertex (0 to %d): ", numVertices - 1);
    scanf("%d", &startVertex);

    printf("Depth First Search starting from vertex %d:\n", startVertex);
    DFS(graph, visited, startVertex, numVertices);

    return 0;
}

// Depth First Search function
void DFS(int graph[MAX][MAX], int visited[MAX], int vertex, int numVertices) {
    printf("%d ", vertex);
    visited[vertex] = 1; // Mark the vertex as visited

    // Explore adjacent vertices
    for (int i = 0; i < numVertices; i++) {
        if (graph[vertex][i] == 1 && !visited[i]) {
            DFS(graph, visited, i, numVertices);
        }
    }
}
