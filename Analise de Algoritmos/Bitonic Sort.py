def compare_and_swap(arr, i, j, direction):
    """
    Compara e troca os elementos se não estiverem na ordem desejada.
    'direction' define se é ordem crescente (True) ou decrescente (False).
    """
    if direction == (arr[i] > arr[j]):
        # Troca os elementos se estiverem na ordem errada
        arr[i], arr[j] = arr[j], arr[i]

def bitonic_merge(arr, low, cnt, direction):
    """
    Mescla uma sequência bitônica no array.
    """
    if cnt > 1:
        mid = cnt // 2
        for i in range(low, low + mid):
            compare_and_swap(arr, i, i + mid, direction)
        # Chama recursivamente para mesclar as duas metades
        bitonic_merge(arr, low, mid, direction)
        bitonic_merge(arr, low + mid, mid, direction)

def bitonic_sort_recursive(arr, low, cnt, direction):
    """
    Função recursiva para dividir o array em sequências bitônicas.
    """
    if cnt > 1:
        mid = cnt // 2
        # Ordena a primeira metade em ordem crescente
        bitonic_sort_recursive(arr, low, mid, True)
        # Ordena a segunda metade em ordem decrescente
        bitonic_sort_recursive(arr, low + mid, mid, False)
        # Mescla as duas sequências
        bitonic_merge(arr, low, cnt, direction)

def bitonic_sort(arr, n):
    """
    Função principal que chama a recursiva e imprime o estado em cada refinamento.
    """
    print(f"Vetor inicial: {arr}")
    bitonic_sort_recursive(arr, 0, n, True)
    print(f"Vetor ordenado: {arr}")

# Função para executar o código e imprimir refinamentos
def print_refinamentos(arr):
    """
    Função principal para executar o bitonic sort com impressões.
    """
    n = len(arr)
    bitonic_sort(arr, n)

# Exemplo
arr = [2, 3, 4, 5, 1, 7, 8, 9, 10, 6]
print_refinamentos(arr)
