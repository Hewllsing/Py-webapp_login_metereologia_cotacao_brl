class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.definir_nota(nota)

    def definir_nota(self, nota):
        if not isinstance(nota, (int,float)):
            raise ValueError("A nota tem que er um numero inteiro ou flutuante.")
        
        if nota < 0 or nota > 20:
            raise ValueError("A nota tem que ser entre 0 e 20.")
        
        self.nota = nota

    def situacao(self):
        if self.esta_aprovado:
            print("Aprovado")
        else:
            print("Reprovado")


    def esta_aprovado(self):
        if self.nota >= 10:
            return True
        else:
            return False

    def nome_formatado(self):
        info = "Nome: " + self.nome + " | " + "Nota: " + str(self.nota)
        print(info)
    
    
    def resumo(self):
        return self.nome_formatado(), self.situacao()


    def alterar_nota(self, novaNota):
        self.nota = novaNota
        return print(f"Nota alterada!")
    

    def adicionar_pontos(self, add):
        self.nota = add + self.nota
        return print("Pontos adicionados!")
    

    def comparar_nota(self, outro_aluno):
        if self.nota > outro_aluno.nota:
            print(self.nome_formatado())
            print("Aluno local")
        else:
            print(outro_aluno.nome_formatado())
            print("É maior!")
