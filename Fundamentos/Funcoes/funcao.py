# Função que exibe informações sobre o autor e a versão do programa
def sobre(versao):
    print("=" * 30)
    print("Autor: Leonardo Souza")
    print(f"Versão: {versao}")
    print("=" * 30)

# Armazena a versão do programa
versao_do_programa = "2.03"

print("Inicio")
# Chama a função passando a versão como argumento
sobre(versao_do_programa)
print("Fim")


# Função que recebe três números e retorna seus valores ao cubo
# Em Python, uma função pode retornar múltiplos valores
def cubo(num1, num2, num3):
    return num1 ** 3, num2 ** 3, num3 ** 3

# Chama a função e armazena os três retornos em uma tupla
numero = cubo(2, 3, 4)

# Exibe o resultado
print(numero)
