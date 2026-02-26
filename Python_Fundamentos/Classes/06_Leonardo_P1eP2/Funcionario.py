# Passo 1
class Funcionario():
    def __init__(self, nome, salario_base):
        self.__nome = nome
        self.salario = salario_base

# Passo 2
    @property
    def nome(self):
        return self.__nome
    
    
    @property
    def salario(self):
        return self.__salario
        

    @salario.setter
    def salario(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("O salário tem de ser um número (int ou float).")
        if valor < 0:
            raise ValueError("O salário não pode ser negativo.")
        self.__salario = valor


# Passo 3
    def salario_total(self):
        return self.__salario
    

    def resumo(self):
        return f"Nome: {self.nome} | Salario Base: {self.salario} €"
    


# Passo 4
f = Funcionario("Ana", 1200)
print(f.nome) # Esperado: Ana
print(f.salario) # Esperado: 1200.0
print(f.salario_total()) # Esperado: 1200.0
print(f.resumo()) # Esperado: "Nome: Ana | Salario Base: 1200.00€"

# ================= PARTE 2 ===================================================
# Passo 5
