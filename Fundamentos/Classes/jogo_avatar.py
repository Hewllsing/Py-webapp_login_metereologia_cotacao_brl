# Classe que representa um Avatar no jogo
class Avatar:
    def __init__(self, user, mana):
        # Nome do jogador
        self.nome = user
        
        # Energia inicial do avatar
        self.energia = mana
        
        # Dinheiro inicial do avatar
        self.dinheiro = 100

    # Método para alimentar o avatar (custa dinheiro)
    def alimenta(self):
        self.dinheiro -= 10  # Reduz 10 unidades de dinheiro

    # Movimento para a direita (gasta energia)
    def move_direita(self):
        self.energia -= 5     # Consome 5 pontos de energia
        print("Move direita...")
    
    # Movimento para a esquerda (gasta energia)
    def move_esquerda(self):
        self.energia -= 5     # Consome 5 pontos de energia
        print("Move esquerda...")
