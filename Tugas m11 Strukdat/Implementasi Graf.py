from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def printGraph(self):
        for node in self.graph:
            print("Adjacency list of vertex", node)
            print("head", end="")
            for neighbor in self.graph[node]:
                print(" ->", neighbor, end="")
            print("\n")

# Contoh penggunaan Graf
graph = Graph()

edges = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]
for edge in edges:
    graph.addEdge(edge[0], edge[1])

print("Adjacency List Representation of Graph:")
graph.printGraph()
