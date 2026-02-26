from dataclasses import dataclass, field

@dataclass
class Funcionario:
    _nome: str
    _salario: float = field(repr=False)


    def __post_init__(self):
        self.salario = self._salario


    @property
    def nome(self):
        return self._nome
    

    @property
    def salario(self):
        return self._salario
    

    @salario.setter 
    def salario(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("O salario tem que ser int ou float")
        if valor < 0:
            raise ValueError("O salario nao pode ser negativo")
        self._salario = float(valor)


    def salario_total(self):
        return self._salario
    

    def resumo(self):
        return f"Nome: {self.nome} | Salario Base: {self.salario} €"
    

f = Funcionario("Ana", 1200)
print(f.nome) # Esperado: Ana
print(f.salario) # Esperado: 1200.0
print(f.salario_total()) # Esperado: 1200.0
print(f.resumo()) # Esperado: "Nome: Ana | Salario Base: 1200.00€"