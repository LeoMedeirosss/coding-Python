def compAndSwap(a, i, j, dire):
    """
    Compara e troca os elementos em índices i e j do array a.
    Se dire é 1, a troca acontece se a[i] > a[j] (ordem crescente).
    Se dire é 0, a troca acontece se a[i] < a[j] (ordem decrescente).
    """
    if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]  # Realiza a troca

def bitonicMerge(a, low, cnt, dire):
    """
    Mescla uma sequência bitônica no array a.
    low é o índice inicial da sequência a ser mesclada,
    cnt é o número de elementos a serem mesclados,
    e dire indica a ordem (1 para crescente, 0 para decrescente).
    """
    if cnt > 1:  # Continua enquanto houver mais de um elemento
        k = cnt // 2  # Divide a sequência em duas metades
        for i in range(low, low + k):
            compAndSwap(a, i, i + k, dire)  # Compara e troca os elementos
        bitonicMerge(a, low, k, dire)  # Mescla a primeira metade
        bitonicMerge(a, low + k, k, dire)  # Mescla a segunda metade

def bitonicSort(a, low, cnt, dire):
    """
    Ordena o array a de forma bitônica.
    low é o índice inicial da parte do array a ser ordenada,
    cnt é o número de elementos a serem ordenados,
    e dire indica a ordem (1 para crescente, 0 para decrescente).
    """
    if cnt > 1:  # Continua enquanto houver mais de um elemento
        k = cnt // 2  # Divide a sequência em duas metades
        bitonicSort(a, low, k, 1)  # Ordena a primeira metade em ordem crescente
        bitonicSort(a, low + k, k, 0)  # Ordena a segunda metade em ordem decrescente
        bitonicMerge(a, low, cnt, dire)  # Mescla as duas metades ordenadas
        print(f"Após chamada de bitonicMerge em {low}, {cnt}: {a}")  # Imprime o estado atual do array

def sort(a, N, up):
    """
    Função de chamada para ordenar o array a.
    N é o número total de elementos,
    e up indica a ordem (1 para crescente).
    """
    bitonicSort(a, 0, N, up)  # Inicia o processo de ordenação

# Código para testar a função
a = [3, 7, 4, 8, 6, 2, 1, 5, 10, 9, 12, 11, 16, 15, 14, 13]  # Array a ser ordenado
n = len(a)  # Número de elementos no array
up = 1  # Indica que a ordenação será em ordem crescente

print("Vetor inicial:")
print(a)  # Imprime o array inicial
sort(a, n, up)  # Chama a função de ordenação
print("\nVetor ordenado:")
print(a)  # Imprime o array após a ordenação