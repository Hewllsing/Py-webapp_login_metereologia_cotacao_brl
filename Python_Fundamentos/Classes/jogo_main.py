# Importa a classe Avatar do módulo jogo_avatar
from jogo_avatar import Avatar

# Cria dois jogadores (instâncias da classe Avatar)
player1 = Avatar("Leo", 70)
player2 = Avatar("Jheny", 70)

# ---------------------------
# Ações do player1 (consome energia e ganha dinheiro)
# ---------------------------

# Player 1 se alimenta (provavelmente aumenta energia)
player1.alimenta()

# Movimentos que devem consumir energia
player1.move_direita()
player1.move_esquerda()
player1.move_direita()

# Player 1 se alimenta novamente
player1.alimenta()

# Mais movimentos
player1.move_direita()
player1.move_esquerda()
player1.move_direita()

# ---------------------------
# Exibindo os dados finais do player1
# ---------------------------
print(f"Nome: {player1.nome}")
print(f"Energia: {player1.energia}")
print(f"Dinheiro: {player1.dinheiro}")

# ---------------------------
# Exibindo os dados finais do player2 (que não realizou ações)
# ---------------------------
print(f"Nome: {player2.nome}")
print(f"Energia: {player2.energia}")
print(f"Dinheiro: {player2.dinheiro}")
