try:
    idade = int(input("Idade: "))
    print(idade)
    salario = 1600
    risco = salario / idade
except ValueError:
    print("A idade introduzida não é válida!")
except ZeroDivisionError: 
    print("A idade não pode ser ZERO!")
print("FIM")