# Algoritmo do Caminho Hamiltoniano

Este projeto implementa um algoritmo para encontrar um **Caminho Hamiltoniano** em um grafo dirigido ou não dirigido.
Um Caminho Hamiltoniano é uma sequência de vértices que visita cada vértice exatamente uma vez.
Este problema está relacionado ao Problema do Caixeiro Viajante (TSP) e é conhecido por ser NP-completo.

## Lógica da implementação 

```python
class Graph:
    def __init__(self, n, directed=False):
        self.n = n
        self.directed = directed
        self.adj = [[] for _ in range(n)]
```

#### Cria uma classe Graph que representa o grafo com:

- `n`: número de vértices
- `directed`: indica se o grafo é dirigido
- `adj`: lista de adjacência para representar as arestas
 
***

```python
    def add_edge(self, u, v):
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)
```
#### Adiciona uma aresta:
- Se o grafo **não for dirigido**, adiciona nos dois sentidos.
- Se for **dirigido**, adiciona apenas de `u` para `v`.

***

```python
    def show(self):
        tipo = "Dirigido" if self.directed else "Não dirigido"
        print(f"Grafo {tipo}:")
        for i in range(self.n):
            print(f"  {i} -> {self.adj[i]}")
        print()
```
#### Imprime a estrutura do grafo (lista de adjacência).

***

```python
def hamiltonian_path(graph):
    n = graph.n
```
#### Função que tenta encontrar um Caminho Hamiltoniano para o grafo informado.

***

```python
    def backtrack(v, visited, path):
        if len(path) == n:
            return path
```
#### Função recursiva de backtracking:
- Se o número de vértices visitados `(len(path))` for igual a `n`, o caminho cobre todos os vértices.

***

```python
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
```
#### Explora cada vizinho não visitado:
- Tenta visitar todos os vizinhos de v que ainda não foram visitados.
- Adiciona o vizinho ao caminho e continua recursivamente.
- Se não encontrar solução, desfaz a última escolha (backtracking).

***

```python
    for start in range(n):
        visited = {start}
        path = [start]
        result = backtrack(start, visited, path)
        if result:
            return result
    return None
```
#### Tenta iniciar o caminho a partir de cada vértice:
- Tenta iniciar o caminho por cada vértice possível.
- Retorna o caminho assim que encontrar um válido.
- Se nenhum caminho for encontrado, retorna `None`.

## Exemplo de execução

```python
if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(3, 4)

    g.show()

    path = hamiltonian_path(g)
    if path:
        print("Caminho Hamiltoniano encontrado:")
        print(" -> ".join(map(str, path)))
    else:
        print("Nenhum Caminho Hamiltoniano encontrado.")
```

## Como executar o projeto
1. Clone o repositório
```bash
    git clone https://github.com/Frederico-dos-Santos/hamiltonian-path.git
```

2. Instale as dependências
```bash
    pip install networkx matplotlib
```

3. Execute o código
```bash
    python3 main.py
```

4. Saída esperada

```python
=== Grafo NÃO DIRIGIDO ===
Grafo Não dirigido:
  0 -> [1, 2]
  1 -> [0, 2]
  2 -> [1, 3, 0]
  3 -> [2, 4]
  4 -> [3]

Caminho Hamiltoniano: [0, 1, 2, 3, 4]

=== Grafo DIRIGIDO ===
Grafo Dirigido:
  0 -> [1, 2]
  1 -> [2]
  2 -> [3]
  3 -> []

Caminho Hamiltoniano: [0, 1, 2, 3]
```

#### Visualização do Caminho Hamiltoniano
O grafo e o caminho Hamiltoniano encontrado serão visualizados em uma janela gráfica, onde o caminho será destacado em vermelho.

## Análise de Complexidade 
### Classes de Complexidade (P, NP, NP-Completo e NP-Difícil)
O problema do Caminho Hamiltoniano pertence à classe NP-Completo, pois:
- `Está em NP`: Dado um caminho, é possível verificar em tempo polinomial se ele é Hamiltoniano (basta checar se cada vértice aparece uma vez e se as arestas existem).
- `É NP-Difícil`: Não se conhece um algoritmo de tempo polinomial para encontrar um Caminho Hamiltoniano em todos os grafos.
- `É NP-Completo`: Como está em NP e é NP-Difícil, o problema do Caminho Hamiltoniano é NP-Completo.

- O `Problema do Caixeiro Viajante (TSP)` é um problema generalizado do Caminho Hamiltoniano. O TSP adiciona custos (pesos) às arestas e procura o `menor caminho`. Já o Caminho Hamiltoniano só verifica `se um caminho que passa por todos os vértices existe`. Assim, o Caminho Hamiltoniano é `NP-Completo`, e o TSP é `NP-Difícil`.

### Complexidade Assintótica de Tempo
O algoritmo usa backtracking puro, tentando todas as combinações possíveis de vértices. Portanto, a complexidade de tempo é `O(N!)`, onde N é o número de vértices no grafo. Isso ocorre porque:
- o número de caminhos possíveis cresce fatorialmente com o número de vértices;
- o algoritmo testa recursivamente cada possibilidade até encontrar um caminho válido ou esgotar todas as opções. 
- Método usado: `contagem de operações por expansão combinatória`, o número de possibilidades é o número de permutações de n vértices.

### Aplicação do Teorema Mestre
O Teorema Mestre é usado para resolver recorrências do tipo `T(n) = aT(n/b) + f(n)`, onde há subproblemas independentes de tamanho reduzido. No entanto, o algoritmo de backtracking para o Caminho Hamiltoniano não se encaixa nesse formato, pois não divide o problema em subproblemas independentes de tamanho reduzido. Em vez disso, ele explora todas as combinações possíveis de vértices, o que leva a uma complexidade fatorial. Portanto, `o Teorema Mestre não é aplicável neste caso`.

### Casos de Complexidade
- `Melhor Caso`: O melhor caso ocorre quando o primeiro caminho testado já é Hamiltoniano. Neste caso, a complexidade seria `O(N)`, pois o algoritmo visitaria cada vértice uma vez.
- `Caso Médio`: No caso médio, o algoritmo ainda precisa explorar uma grande parte das combinações possíveis, levando a uma complexidade próxima de `O(k·n)`, onde `k` representa o número de caminhos parciais testados. Esse valor depende da estrutura do grafo e da ordem em que os vértices são explorados.
- `Pior Caso`: O pior caso ocorre quando o algoritmo precisa explorar todas as permutações possíveis de vértices antes de concluir que não existe um Caminho Hamiltoniano. Isso leva a uma complexidade de `O(N!)`, onde `N` é o número de vértices no grafo.

#### Impacto de Desempenho
- Em grafos pequenos `N < 10`, o algoritmo pode ser executado em tempo razoável.
- Em grafos maiores, o tempo de execução cresce rapidamente devido à complexidade fatorial, tornando o algoritmo impraticável computacionalmente.
