from collections import defaultdict

# Classe para representar um grafo não-direcionado com pesos nas arestas
class Graph:
 
    def __init__(self, vertices):
        self.V = vertices  # Número de vértices no grafo
        self.graph = []  # Lista para armazenar as arestas do grafo (cada aresta é uma tupla [u, v, w])
         
    # Função para adicionar uma aresta ao grafo com um peso específico
    #u: Um dos vértices conectados pela aresta.
    #v: O outro vértice conectado pela mesma aresta.
    #w: O peso ou custo associado a essa aresta, que representa a "distância" ou "custo" para ir de u até v.
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
    # Função para encontrar o "pai" do conjunto de um elemento i (com compressão de caminho)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
 
    # Função para unir dois conjuntos x e y usando união por rank
    def union(self, parent, rank, x, y):
        # Encontra as raízes dos conjuntos de x e y
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        # Anexa a árvore de menor rank na raiz da árvore de maior rank
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        # Se os ranks são iguais, faz um deles raiz e incrementa o rank dessa raiz
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
        #Se o conjunto de x tem menor rank (altura), ele é anexado ao conjunto de y.
        #Se o conjunto de y tem menor rank, ele é anexado ao conjunto de x.
 
    # Função principal para construir a Árvore Geradora Mínima (MST) usando o algoritmo de Borůvka
    def boruvkaMST(self):
        # Inicializa a estrutura para os pais e os ranks dos subconjuntos de cada vértice
        parent = []
        rank = []
 
        # Array para armazenar a aresta mais barata de cada subconjunto
        cheapest = []
 
        # Inicialmente, consideramos que cada vértice é uma árvore isolada
        numTrees = self.V  # Número de árvores (componentes) diferentes inicialmente
        MSTweight = 0  # Peso total da MST
        
        # Cria V subconjuntos com elementos únicos (inicializa cada vértice como seu próprio pai)
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
            cheapest = [-1] * self.V  # Inicializa a lista de arestas mais baratas de cada componente
 
        # Continua combinando componentes até que todos sejam unidos em uma única árvore MST
        while numTrees > 1:
 
            # Para cada aresta do grafo, encontra a aresta mais barata de cada componente
            for i in range(len(self.graph)):
                u, v, w = self.graph[i]
                set1 = self.find(parent, u)  # Componente do vértice u
                set2 = self.find(parent, v)  # Componente do vértice v
 
                # Se u e v não estão no mesmo conjunto, verifica se a aresta atual é a mais barata
                if set1 != set2:     
                    if cheapest[set1] == -1 or cheapest[set1][2] > w:
                        cheapest[set1] = [u, v, w]  # Atualiza aresta mais barata para set1
                    if cheapest[set2] == -1 or cheapest[set2][2] > w:
                        cheapest[set2] = [u, v, w]  # Atualiza aresta mais barata para set2
 
            # Adiciona as arestas mais baratas selecionadas à MST
            for node in range(self.V):
                if cheapest[node] != -1:  # Verifica se há uma aresta válida
                    u, v, w = cheapest[node]
                    set1 = self.find(parent, u)
                    set2 = self.find(parent, v)
 
                    # Verifica se u e v estão em componentes diferentes (não formando ciclo)
                    if set1 != set2:
                        MSTweight += w  # Adiciona o peso da aresta ao peso total da MST
                        self.union(parent, rank, set1, set2)  # Une os conjuntos set1 e set2
                        print("Aresta %d-%d com peso %d incluída na MST" % (u, v, w))
                        numTrees -= 1  # Reduz o número de componentes isolados
             
            # Reseta o array de arestas mais baratas para a próxima iteração
            cheapest = [-1] * self.V
 
        print("Peso total da MST é %d" % MSTweight)
                           
# Exemplo de uso
# Testando
g = Graph(6)
g.addEdge(0, 1, 4)
g.addEdge(0, 2, 3)
g.addEdge(1, 2, 1)
g.addEdge(1, 3, 2)
g.addEdge(2, 3, 6)
g.addEdge(3, 4, 10)
g.addEdge(4, 5, 7)
g.addEdge(3, 5, 8)
g.addEdge(2, 5, 5)

g.boruvkaMST()

#g = Graph(4)
#g.addEdge(0, 1, 10)
#g.addEdge(0, 2, 6)
#g.addEdge(0, 3, 5)
#g.addEdge(1, 3, 15)
#g.addEdge(2, 3, 4)
 
#g.boruvkaMST()