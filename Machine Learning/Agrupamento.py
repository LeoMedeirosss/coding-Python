import matplotlib.pyplot as plt

# Dados dos usuários
usuarios = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tempo_uso = [120, 90, 150, 70, 130, 180, 95, 140, 160, 110, 125, 170]  # minutos/dia
interacoes = [50, 40, 80, 30, 60, 100, 35, 65, 90, 55, 45, 85]  # ações/dia

# Grupos atribuídos
grupos = [1, 3, 2, 3, 1, 2, 3, 1, 2, 1, 1, 2]

# Cores para cada grupo
cores = {1: 'red', 2: 'blue', 3: 'green'}
colores_usuarios = [cores[grupo] for grupo in grupos]

# Criar o gráfico de dispersão
plt.figure(figsize=(8, 6))
plt.scatter(tempo_uso, interacoes, c=colores_usuarios, s=100, edgecolors='black')

# Adicionar rótulos aos pontos
for i, usuario in enumerate(usuarios):
    plt.text(tempo_uso[i] + 1, interacoes[i] - 3, f'U{usuario}', fontsize=9)

# Configurar os eixos
plt.xlabel('Tempo médio de uso (min/dia)')
plt.ylabel('Número de interações (ações/dia)')
plt.title('Gráfico de dispersão dos usuários com base no uso diário e interações')

# Exibir o gráfico
plt.grid(True)
plt.show()
