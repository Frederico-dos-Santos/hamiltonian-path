import networkx as nx
import matplotlib.pyplot as plt


def visualizar_grafo(graph, caminho=None):
    """Desenha o grafo e destaca o caminho Hamiltoniano (se existir)."""
    G = nx.DiGraph() if graph.directed else nx.Graph()

    for u in range(graph.n):
        for v in graph.adj[u]:
            G.add_edge(u, v)

    pos = nx.spring_layout(G, seed=42)  

    nx.draw(G, pos, with_labels=True, node_color="lightgray", node_size=800, font_size=10)
    nx.draw_networkx_edges(G, pos, width=1, edge_color="gray")

    if caminho:
        edges_path = [(caminho[i], caminho[i+1]) for i in range(len(caminho) - 1)]
        nx.draw_networkx_edges(G, pos, edgelist=edges_path, width=3, edge_color="red")
        nx.draw_networkx_nodes(G, pos, nodelist=caminho, node_color="lightcoral")

    plt.title("Caminho Hamiltoniano" if caminho else "Nenhum Caminho Hamiltoniano encontrado")
    plt.show()
