# Solicita que o usuário insira um número
numero = int(input("Insira um número: "))

# Verifica se o número é par usando o operador módulo (%)
# Se o resto da divisão por 2 for zero, o número é par
if numero % 2 == 0:
    print(f"Esse numero({numero}) é PAR.")
else:
    # Caso contrário, o número é ímpar
    print(f"Esse numero({numero}) é IMPAR.")
