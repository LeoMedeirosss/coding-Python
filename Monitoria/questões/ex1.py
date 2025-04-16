nomes = []
notas = []
soma = 0

for i in range(5):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    nomes.append(nome)
    notas.append(nota)

for nota in notas:
    soma += nota

media = soma / len(notas)

print(f"\nMédia da turma: {media:.1f}")

print("Alunos acima da média:", end=" ")

acima_da_media = []
for i in range(len(notas)):
    if notas[i] > media:
        acima_da_media.append(nomes[i])

print(", ".join(acima_da_media))