# Solicita que o usuário digite uma frase
frase = str(input("Insira uma frase para contar as vogais: "))

# Define as vogais que queremos contar
vogais = "aeiou"

# Variável que armazenará o total de vogais
contador = 0

# Percorre cada letra da frase transformada para minúsculas
for i in frase.lower():
    # Verifica se a letra atual é uma vogal
    if i in vogais:
        contador += 1  # Se for, incrementa o contador

# Exibe o total de vogais encontradas
print(f"A quantidade de vogais é: {contador}")
