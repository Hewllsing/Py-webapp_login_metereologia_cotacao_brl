from classe_aluno import Aluno

class AlunoBolseiro(Aluno): 
    def __init__(self, nome, nota, bolsa):
        super().__init__(nome, nota) # Construtor da classe pai (Aluno)

        if bolsa < 0:
            raise ValueError("A bolsa não pode ser negativa.")
        self.bolsa = bolsa


    def resumo(self):
        # Sobrescreve a função resumo do pai (Override)
        return print(f"{super().resumo()} (Bolsa: {self.bolsa} €)")