def compAndSwap(a, i, j, dire):
    if (dire == 1 and a[i] > a[j]) or (dire == 0 and a[i] < a[j]):
        a[i], a[j] = a[j], a[i]

def bitonicMerge(a, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            compAndSwap(a, i, i + k, dire)
        bitonicMerge(a, low, k, dire)
        bitonicMerge(a, low + k, k, dire)

def bitonicSort(a, low, cnt, dire):
    if cnt > 1:
        k = cnt // 2
        bitonicSort(a, low, k, 1)  # Ordena a primeira metade em ordem crescente
        bitonicSort(a, low + k, k, 0)  # Ordena a segunda metade em ordem decrescente
        bitonicMerge(a, low, cnt, dire)
        print(f"Após chamada de bitonicMerge em {low}, {cnt}: {a}")  # Imprime após mesclagem

def sort(a, N, up):
    bitonicSort(a, 0, N, up)

# Código para testar a função
a = [3, 7, 4, 8, 6, 2, 1, 5, 10, 9, 12, 11, 16, 15, 14, 13]
n = len(a)
up = 1

print("Vetor inicial:")
print(a)
sort(a, n, up)
print("\nVetor ordenado:")
print(a)
