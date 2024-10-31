from collections import defaultdict
 
# Classe para representar um grafo
class Graph:
 
    def __init__(self, vertices):
        self.V = vertices  # Número de vértices
        self.graph = []  # dicionário padrão para armazenar o grafo
         
    # Função para adicionar uma aresta ao grafo
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
    # Função utilitária para encontrar o conjunto de um elemento i
    # (usa a técnica de compressão de caminho)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    # Função para unir dois conjuntos x e y
    # (usa união por rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Anexa a árvore de menor rank na raiz da árvore de maior rank
        # (União por Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        # Se os ranks são iguais, então faz um deles como raiz e incrementa
        # seu rank em um
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
 
    # Função principal para construir a MST usando o algoritmo de Borůvka
    def boruvkaMST(self):
        parent = []
        rank = []
 
        # Um array para armazenar o índice da aresta mais barata de cada
        # subconjunto. Ele armazena [u, v, w] para cada componente
        cheapest = []
 
        # Inicialmente, existem V árvores diferentes.
        # Finalmente, haverá uma árvore única, que será a MST
        numTrees = self.V
        MSTweight = 0
 
        # Cria V subconjuntos com elementos únicos
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
            cheapest = [-1] * self.V
     
        # Continua combinando componentes (ou conjuntos) até que todos
        # os componentes sejam combinados em uma única MST
        while numTrees > 1:
 
            # Percorre todas as arestas e atualiza
            # a aresta mais barata de cada componente
            for i in range(len(self.graph)):
 
                # Encontra os componentes (ou conjuntos) das duas extremidades
                # da aresta atual
                u, v, w = self.graph[i]
                set1 = self.find(parent, u)
                set2 = self.find(parent, v)
 
                # Se as duas extremidades da aresta atual pertencem ao
                # mesmo conjunto, ignora essa aresta. Caso contrário,
                # verifica se a aresta atual é a mais próxima
                # das arestas mais baratas dos conjuntos set1 e set2
                if set1 != set2:     
                    if cheapest[set1] == -1 or cheapest[set1][2] > w:
                        cheapest[set1] = [u, v, w] 
                    if cheapest[set2] == -1 or cheapest[set2][2] > w:
                        cheapest[set2] = [u, v, w]
 
            # Considera as arestas mais baratas selecionadas e as adiciona
            # à MST
            for node in range(self.V):
 
                # Verifica se a aresta mais barata para o conjunto atual existe
                if cheapest[node] != -1:
                    u, v, w = cheapest[node]
                    set1 = self.find(parent, u)
                    set2 = self.find(parent, v)
 
                    if set1 != set2:
                        MSTweight += w
                        self.union(parent, rank, set1, set2)
                        print("Aresta %d-%d com peso %d incluída na MST" % (u, v, w))
                        numTrees -= 1
             
            # Reseta o array de arestas mais baratas
            cheapest = [-1] * self.V
 
        print("Peso da MST é %d" % MSTweight)
                           
 
# Exemplo de uso
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
 
g.boruvkaMST()