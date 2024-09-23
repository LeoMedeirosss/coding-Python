def compare_and_swap(arr, i, j, direction):
    """
    Compara e troca os elementos se não estiverem na ordem desejada.
    'direction' define se é ordem crescente (True) ou decrescente (False).
    """
    if direction == (arr[i] > arr[j]):
        arr[i], arr[j] = arr[j], arr[i]

def bitonic_merge(arr, low, cnt, direction):
    """
    Mescla uma sequência bitônica no array.
    """
    if cnt > 1:
        mid = cnt // 2
        for i in range(low, low + mid):
            compare_and_swap(arr, i, i + mid, direction)
        print(f"Após mesclagem: {arr}")  # Imprime o vetor após mesclagem
        bitonic_merge(arr, low, mid, direction)
        bitonic_merge(arr, low + mid, mid, direction)

def bitonic_sort_recursive(arr, low, cnt, direction):
    """
    Função recursiva para dividir o array em sequências bitônicas.
    """
    if cnt > 1:
        mid = cnt // 2
        bitonic_sort_recursive(arr, low, mid, True)  # Primeira metade em ordem crescente
        bitonic_sort_recursive(arr, low + mid, mid, False)  # Segunda metade em ordem decrescente
        bitonic_merge(arr, low, cnt, direction)  # Mescla as duas sequências
        print(f"Após chamada de bitonic_merge em {low}, {cnt}: {arr}")

def bitonic_sort(arr):
    """
    Função principal que chama a recursiva e imprime o estado em cada refinamento.
    """
    print(f"Vetor inicial: {arr}")
    bitonic_sort_recursive(arr, 0, len(arr), True)
    print(f"Vetor ordenado: {arr}")

# Exemplo
arr = [3, 7, 4, 8, 6, 2, 10, 5, 9, 1]
bitonic_sort(arr)