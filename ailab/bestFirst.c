#include <stdio.h>
#include <stdlib.h>

// Structure for representing a node in the graph
typedef struct Node {
    int vertex;
    int heuristic;
} Node;

// Structure for a priority queue
typedef struct PriorityQueue {
    Node *arr;
    int size;
} PriorityQueue;

// Function to create a new priority queue
PriorityQueue* createPriorityQueue(int capacity) {
    PriorityQueue *pq = (PriorityQueue*)malloc(sizeof(PriorityQueue));
    pq->arr = (Node*)malloc(sizeof(Node) * capacity);
    pq->size = 0;
    return pq;
}

// Function to swap two nodes in the priority queue
void swap(Node *a, Node *b) {
    Node temp = *a;
    *a = *b;
    *b = temp;
}

// Function to min-heapify the priority queue based on heuristic
void heapify(PriorityQueue *pq, int i) {
    int smallest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < pq->size && pq->arr[left].heuristic < pq->arr[smallest].heuristic) {
        smallest = left;
    }
    if (right < pq->size && pq->arr[right].heuristic < pq->arr[smallest].heuristic) {
        smallest = right;
    }
    if (smallest != i) {
        swap(&pq->arr[i], &pq->arr[smallest]);
        heapify(pq, smallest);
    }
}

// Function to insert a node into the priority queue
void insert(PriorityQueue *pq, int vertex, int heuristic) {
    pq->arr[pq->size].vertex = vertex;
    pq->arr[pq->size].heuristic = heuristic;
    pq->size++;
    for (int i = pq->size / 2 - 1; i >= 0; i--) {
        heapify(pq, i);
    }
}

// Function to extract the node with the minimum heuristic value
Node extractMin(PriorityQueue *pq) {
    Node min = pq->arr[0];
    pq->arr[0] = pq->arr[pq->size - 1];
    pq->size--;
    heapify(pq, 0);
    return min;
}

// Function to perform Best-First Search
void bestFirstSearch(int graph[5][5], int start, int goal, int heuristics[5]) {
    PriorityQueue *pq = createPriorityQueue(5);
    int visited[5] = {0};

    // Insert the start node into the priority queue
    insert(pq, start, heuristics[start]);

    while (pq->size > 0) {
        // Extract the node with the minimum heuristic
        Node current = extractMin(pq);

        if (visited[current.vertex]) {
            continue;
        }

        printf("Visiting node: %d\n", current.vertex);
        visited[current.vertex] = 1;

        // If we reach the goal, terminate the search
        if (current.vertex == goal) {
            printf("Goal found!\n");
            break;
        }

        // Add neighboring nodes to the priority queue
        for (int i = 0; i < 5; i++) {
            if (graph[current.vertex][i] && !visited[i]) {
                insert(pq, i, heuristics[i]);
            }
        }
    }

    free(pq->arr);
    free(pq);
}

int main() {
    // Define a simple graph with 5 nodes
    int graph[5][5] = {
        {0, 1, 1, 0, 0},
        {1, 0, 1, 0, 0},
        {1, 1, 0, 1, 1},
        {0, 0, 1, 0, 1},
        {0, 0, 1, 1, 0}
    };

    // Define heuristic values for each node
    int heuristics[5] = {7, 6, 2, 3, 1};

    int start = 0; // Start node
    int goal = 4;  // Goal node

    // Perform Best-First Search
    bestFirstSearch(graph, start, goal, heuristics);

    return 0;
}

