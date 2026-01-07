import pandas as pd

# Lê o arquivo Excel "Produtos.xlsx" e cria um DataFrame
tabela = pd.read_excel("produtos.xlsx")

# Exibe a tabela original
print(tabela)

# -------------------------------
# Atualizar o multiplicador de imposto
# -------------------------------

# Localiza as linhas onde a coluna "Tipo" é igual a "Serviço"
# e atualiza o valor da coluna "Multiplicador Imposto" para 1.5
tabela.loc[tabela["Tipo"] == "Serviço", "Multiplicador Imposto"] = 1.5

# Cria uma nova coluna calculando o preço final
# (Multiplicador Imposto * Preço Base Original)
tabela["Preço Base Final"] = tabela["Multiplicador Imposto"] * tabela["Preço Base Original"]

# Salva o DataFrame atualizado em um novo arquivo Excel
# index=False evita salvar o índice como uma coluna
tabela.to_excel("ProdutoPandas.xlsx", index=False)

# Lê novamente o arquivo gerado para conferência
tabela_pandas = pd.read_excel("produto_pandas.xlsx")

# Exibe a tabela final após a primeira atualização
print(tabela_pandas)

# -------------------------------
# Nova atualização específica
# -------------------------------

# Atualiza o multiplicador de imposto apenas para o produto "Tablet"
tabela.loc[tabela["Produtos"] == "Tablet", "Multiplicador Imposto"] = 2.1

# Recalcula a coluna de preço final após a alteração
tabela["Preço Base Final"] = tabela["Multiplicador Imposto"] * tabela["Preço Base Original"]

# Salva o novo resultado em outro arquivo Excel
tabela.to_excel("produto_pandas2.xlsx", index=False)
