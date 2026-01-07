# Classe Aluno representa um estudante com nome e nota
class Aluno:
    def __init__(self, nome, nota):
        # Atributo que guarda o nome do aluno
        self.nome = nome
        
        # Atributo que guarda a nota do aluno
        self.nota = nota

    # Método que verifica se o aluno está aprovado ou reprovado
    def situacao(self):
        # Se a nota for maior ou igual a 10 → aprovado
        if self.nota >= 10:
            print(f"{self.nome} você foi Aprovado!")
        else:
            # Caso contrário → reprovado
            print(f"{self.nome} você foi Reprovado!")
