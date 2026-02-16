from classe_aluno import Aluno as a
from classe_filha import AlunoBolseiro as ab


aluno_1 = a("Leonardo", 20)
aluno_2 = a("Maria", 17)
aluno_bolseiro = ab("Leozinho", 12, 120)

aluno_1.resumo()
print(aluno_bolseiro.resumo())
