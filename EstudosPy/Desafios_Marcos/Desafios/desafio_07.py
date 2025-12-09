# Pedir ao utilizador para introduzir o preço de um produto e a respectiva percentagem de desconto
# O programa deverá calcular e mostrar o valor a pagar após desconto
# Caso a informação não seja válida, o programa deverá indicar qual foi o erro.

try:
    # Lê o preço do produto (pode gerar ValueError se não for número)
    preco_produto = float(input("Preço do produto: "))
    
    # Lê a percentagem de desconto
    desconto_produto = float(input("Desconto: "))
    
    # Calcula o valor final após aplicar o desconto
    valor_a_pagar = preco_produto - (preco_produto * (desconto_produto / 100))
    
    # Mostra o valor já com desconto
    print(f"O valor a pagar é: {valor_a_pagar}.")
    
# Trata erro caso o usuário escreva algo que não seja número
except ValueError:
    print("O campo não pode estar vazio, digite apenas números.")

# Trata erro caso haja uma divisão por zero (neste caso não ocorre, mas fica como exemplo)
except ZeroDivisionError:
    print("O número precisa ser acima de 0.")
