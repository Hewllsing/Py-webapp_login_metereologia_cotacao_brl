from dataclasses import dataclass, field
from dataFuncionario import Funcionario

@dataclass
class FuncionarioPremium(Funcionario):
    _premio: float = field(repr=False)


    def __post_init__(self):
        super().__post_init__()
        self.premio = self._premio
    

    @property
    def premio(self):
        return self._premio


    @premio.setter 
    def premio(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("O premio tem que ser int ou float")
        if valor < 0:
            raise ValueError("O premio nao pode ser negativo")
        self._premio = float(valor)


    def salario_total(self):
        return super().salario_total() + self._premio

    def resumo(self):
        return super().resumo() + f" Premio: {self._premio:.2f} | Total: {self.salario_total():.2f}€"


p = FuncionarioPremium("Carlos", 1500, 300)
print(p.nome)           # Carlos
print(p.salario)        # 1500.0 (depende da sua classe Funcionario)
print(p.premio)         # 300.0
print(p.salario_total())# 1800.0
print(p.resumo())       # ... Total: 1800.00€