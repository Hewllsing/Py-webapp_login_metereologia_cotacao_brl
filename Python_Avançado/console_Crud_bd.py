import mysql.connector 

# =============================
# Configurações da Base de Dados
# =============================
HOST = "62.28.39.135"
USER = "efa0125"
PASSWORD = "123.Abc"
DATABASE = "efa0125_25_formacao_crud"

# =============================
# Função para ligar ao MySQL
# =============================
def ligar_bd():
    """
    Cria e retorna uma conexão com a base de dados MySQL
    """
    return mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

# =============================
# CREATE - Inserir Utilizador
# =============================
def inserir_utilizador():
    # Receber dados do utilizador
    nome = input("Nome: ")
    email = input("E-mail: ")

    # Abre conexão com a BD
    cnx = ligar_bd()
    cursor = cnx.cursor()

    # Comando SQL para inserir
    sql = "INSERT INTO utilizadores (nome, email) VALUES (%s, %s)"
    
    # Executa o comando com os parâmetros
    cursor.execute(sql, (nome, email))
    
    # Guarda alterações no BD
    cnx.commit()

    print("Utilizador inserido com sucesso!")

    # Fecha cursor e conexão
    cursor.close()
    cnx.close()


# =============================
# READ - Listar Utilizadores
# =============================
def listar_utilizadores():
    cnx = ligar_bd()
    cursor = cnx.cursor()

    # SQL para obter todos os utilizadores
    sql = "SELECT id, nome, email, created_at FROM utilizadores"
    cursor.execute(sql)

    resultados = cursor.fetchall()

    print("\n--- LISTA DE UTILIZADORES ---")
    
    # Percorre cada linha retornada
    for linha in resultados:
        # linha = (id, nome, email, created_at)
        print(linha)

    cursor.close()
    cnx.close()


# =============================
# UPDATE - Atualizar Utilizador
# =============================
def atualizar_utilizador():
    id_utilizador = input("ID do utilizador a atualizar: ")
    nome_utilizador = input("Novo nome: ")
    email_utilizador = input("Novo e-mail: ")

    cnx = ligar_bd()
    cursor = cnx.cursor()

    # SQL de atualização
    sql = "UPDATE utilizadores SET nome = %s, email = %s WHERE id = %s"
    
    # Executa o SQL com dados
    cursor.execute(sql, (nome_utilizador, email_utilizador, id_utilizador))
    
    cnx.commit()

    print("Utilizador atualizado com sucesso!")

    cursor.close()
    cnx.close()


# =============================
# DELETE - Apagar Utilizador
# =============================
def apagar_utilizador():
    id_utilizador = input("ID do utilizador a apagar: ")

    cnx = ligar_bd()
    cursor = cnx.cursor()

    sql = "DELETE FROM utilizadores WHERE id = %s"
    
    # Quando só há um valor, precisa da vírgula
    cursor.execute(sql, (id_utilizador,))
    
    cnx.commit()

    print("Utilizador apagado com sucesso!")

    cursor.close()
    cnx.close()


# =============================
# MENU PRINCIPAL
# =============================
def menu():
    while True:
        print("\n===== MENU CRUD =====")
        print("1 - Inserir utilizador")
        print("2 - Listar utilizadores")
        print("3 - Atualizar utilizador")
        print("4 - Apagar utilizador")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        # Chama a função conforme a opção
        if opcao == "1":
            inserir_utilizador()
        elif opcao == "2":
            listar_utilizadores()
        elif opcao == "3":
            atualizar_utilizador()
        elif opcao == "4":
            apagar_utilizador()
        elif opcao == "0":
            print("A sair...")
            break
        else:
            print("Opção inválida!")

# =============================
# Execução do Programa
# =============================
menu()
