from Funcionario import Funcionario

class FuncionarioPremium(Funcionario):
    def __init__(self, nome, salario_base, valor):
        super().__init__(nome, salario_base)
        self.premio = valor  # aqui já passa pela validação do setter

    @property
    def premio(self):
        return self.__premio

    @premio.setter
    def premio(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Tem que ser numerico.")
        if valor < 0:
            raise ValueError("Tem que ser positivo.")
        self.__premio = float(valor)

    def salario_total(self):
        return super().salario_total() + self.__premio

    def resumo(self):
        return super().resumo() + f" Premio: {self.__premio:.2f} | Total: {self.salario_total():.2f}€"


p = FuncionarioPremium("Carlos", 1500, 300)
print(p.nome)           # Carlos
print(p.salario)        # 1500.0 (depende da sua classe Funcionario)
print(p.premio)         # 300.0
print(p.salario_total())# 1800.0
print(p.resumo())       # ... Total: 1800.00€