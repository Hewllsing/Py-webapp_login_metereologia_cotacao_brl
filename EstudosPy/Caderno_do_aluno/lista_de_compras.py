# Cria uma lista com 5 posições vazias
frutas = [""] * 5

# Loop para preencher cada posição da lista
for i in range(len(frutas)):
    # Pede ao usuário o nome de uma fruta e coloca na posição correspondente
    frutas[i] = input("Digite o nome de uma fruta para adicionar à lista de compras: ")

# Exibe a lista de compras em formato mais amigável
print("Sua lista de compras contém:")
for fruta in frutas:
    print(f"- {fruta}")

# Exibe a lista completa (estrutura bruta)
print(frutas)
