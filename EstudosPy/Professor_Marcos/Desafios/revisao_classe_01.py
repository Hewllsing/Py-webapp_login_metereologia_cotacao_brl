'''
Exercício de revisão
Exercício de classes em Python
 
Exercício: Classe Aluno
Enunciado

Crie uma classe chamada Aluno que represente um estudante.
A classe deve:
    Ter um construtor (__init__) com os atributos:
        nome
        nota
Ter um método chamado situacao() que:
    Retorne "Aprovado" se a nota for maior ou igual a 10
    Retorne "Reprovado" caso contrário
Depois:
    Crie dois objetos da classe Aluno
    Mostre o nome, a nota e a situação de cada aluno
'''

# Classe que representa um Avatar no jogo
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def situacao(self):
        if self.nota >= 7:
            print(f"{self.nome} você foi Aprovado!")
        else:
            print(f"{self.nome} você foi Reprovado!")
            

