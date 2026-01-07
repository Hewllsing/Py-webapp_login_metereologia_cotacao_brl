# Importa a classe Aluno do arquivo revisao_classe_01.py
from revisao_classe_01 import Aluno

# Exemplo usando inputs (comentado)
# aluno_01 = Aluno(input("Digite seu nome: "), int(input("Digite sua nota: ")))

# Cria dois objetos da classe Aluno com nome e nota
aluno_01 = Aluno("Leo", 15)
aluno_02 = Aluno("Lucas", 7)

# Chama o método situacao() da classe Aluno 
aluno_01.situacao()
aluno_02.situacao()
