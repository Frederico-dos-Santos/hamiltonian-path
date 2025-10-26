from view import visualizar_grafo

class Graph:
    def __init__(self, n, directed=False):
        self.n = n
        self.directed = directed
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def show(self):
        tipo = "Dirigido" if self.directed else "Não dirigido"
        print(f"Grafo {tipo}:")
        for i in range(self.n):
            print(f"  {i} -> {self.adj[i]}")
        print()


def hamiltonian_path(graph):
    n = graph.n

    def backtrack(v, visited, path):
        if len(path) == n:
            return path 

        for neighbor in graph.adj[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                result = backtrack(neighbor, visited, path)
                if result:
                    return result
                visited.remove(neighbor)
                path.pop()
        return None

    for start in range(n):
        visited = {start}
        path = [start]
        result = backtrack(start, visited, path)
        if result:
            return result
    return None

if __name__ == "__main__":

    print("=== Grafo NÃO DIRIGIDO ===")
    g1 = Graph(5, directed=False)
    g1.add_edge(0, 1)
    g1.add_edge(1, 2)
    g1.add_edge(2, 3)
    g1.add_edge(3, 4)
    g1.add_edge(0, 2)
    g1.show()
    caminho1 = hamiltonian_path(g1)
    print("Caminho Hamiltoniano:", caminho1, "\n")
    visualizar_grafo(g1, caminho1)

    print("=== Grafo DIRIGIDO ===")
    g2 = Graph(4, directed=True)
    g2.add_edge(0, 1)
    g2.add_edge(1, 2)
    g2.add_edge(2, 3)
    g2.add_edge(0, 2)
    g2.show()
    caminho2 = hamiltonian_path(g2)
    print("Caminho Hamiltoniano:", caminho2)
    visualizar_grafo(g2, caminho2)
