#include <stdio.h>
#include <stdlib.h>

#define MAX 100  // Maximum number of vertices

int adj[MAX][MAX]; // Adjacency matrix
int visited[MAX];  // Visited array for BFS
int queue[MAX];    // Queue for BFS traversal
int front = -1, rear = -1;

// Enqueue function
void enqueue(int vertex) {
    if (rear == MAX - 1) {
        printf("Queue is full!\n");
        return;
    }
    if (front == -1) front = 0;
    queue[++rear] = vertex;
}

// Dequeue function
int dequeue() {
    if (front == -1 || front > rear) {
        printf("Queue is empty!\n");
        return -1;
    }
    return queue[front++];
}

// BFS function
void bfs(int start, int n) {
    printf("Breadth First Search starting from vertex %d:\n", start);
    enqueue(start);
    visited[start] = 1;

    while (front <= rear) {
        int current = dequeue();
        printf("%d ", current);

        // Traverse all adjacent vertices
        for (int i = 0; i < n; i++) {
            if (adj[current][i] == 1 && !visited[i]) {
                enqueue(i);
                visited[i] = 1;
            }
        }
    }
    printf("\n");
}

// Main function
int main() {
    int n, start;

    printf("Enter the number of vertices in the graph: ");
    scanf("%d", &n);

    printf("Enter the adjacency matrix of the graph:\n");
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &adj[i][j]);
        }
    }

    printf("Enter the starting vertex (0 to %d): ", n - 1);
    scanf("%d", &start);

    // Initialize visited array
    for (int i = 0; i < n; i++) {
        visited[i] = 0;
    }

    // Perform BFS
    bfs(start, n);

    return 0;
}
