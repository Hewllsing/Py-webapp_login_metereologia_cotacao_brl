# Pede ao usuário um número para gerar a tabuada
numero = int(input("Digite um número para ver a tabuada: "))

# Pede quantas vezes o número será multiplicado
quantidadeMultiplicada = int(input("Digite a quantidade de vezes que você quer multiplicar: "))

# Loop que vai de 1 até a quantidade escolhida
for i in range(1, quantidadeMultiplicada+1):
    # Calcula o resultado da multiplicação
    resultado = numero * i
    
    # Exibe o cálculo no formato de tabuada
    print(f"{numero} x {i} = {resultado}")
