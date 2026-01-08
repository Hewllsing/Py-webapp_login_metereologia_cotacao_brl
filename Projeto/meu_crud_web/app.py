# ---------------------------------------------------
# Imports
# ---------------------------------------------------
from flask import Flask, render_template, request, redirect
import mysql.connector


# ---------------------------------------------------
# Função para ligar à base de dados MySQL
# ---------------------------------------------------
def ligar_bd():
    """
    Cria e retorna a conexão com o servidor MySQL.
    """
    return mysql.connector.connect(
        host="62.28.39.135",
        user="efa0125",
        password="123.Abc",
        database="efa0125_25_formacao_crud"
    )


# ---------------------------------------------------
# Inicialização do Flask
# ---------------------------------------------------
app = Flask(__name__)


# ---------------------------------------------------
# Rota principal (lista utilizadores)
# ---------------------------------------------------
@app.route("/")
def index():
    # Conectar à base de dados
    cnx = ligar_bd()
    
    # cursor(dictionary=True) retorna cada linha como dicionário
    cursor = cnx.cursor(dictionary=True)

    # Buscar utilizadores ordenados do mais recente para o mais antigo
    cursor.execute("SELECT id, nome, email, created_at FROM utilizadores ORDER BY id DESC")
    utilizadores = cursor.fetchall()

    # Fechar cursor e conexão
    cursor.close()
    cnx.close()

    # Renderizar o template passando os dados para o HTML
    return render_template("index.html", utilizadores=utilizadores)


# ---------------------------------------------------
# Rota para criar novo utilizador
# ---------------------------------------------------
@app.route("/novo", methods=["GET", "POST"])
def novo():

    # Quando o formulário é submetido (POST)
    if request.method == "POST":
        
        # Obter valores enviados pelo formulário
        nome = request.form["nome"]
        email = request.form["email"]

        # Conectar ao banco
        cnx = ligar_bd()
        cursor = cnx.cursor()

        # Inserir novo utilizador na tabela
        cursor.execute(
            "INSERT INTO utilizadores (nome, email) VALUES (%s, %s)", 
            (nome, email)
        )
        cnx.commit()  # salvar no banco

        # Encerrar conexão
        cursor.close()
        cnx.close()

        # Redirecionar para a página inicial
        return redirect("/")

    # Caso seja GET, exibir formulário vazio
    return render_template("form.html", titulo="Novo utilizador", utilizador=None)


# ---------------------------------------------------
# Rota para editar utilizador
# ---------------------------------------------------
@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_utilizador(id):

    # Conectar ao banco
    cnx = ligar_bd()
    cursor = cnx.cursor(dictionary=True)

    # Se o formulário foi enviado (POST)
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]

        # Atualizar dados no banco
        cursor2 = cnx.cursor()
        cursor2.execute(
            "UPDATE utilizadores SET nome = %s, email = %s WHERE id = %s", 
            (nome, email, id)
        )
        cnx.commit()

        # Fechar conexões
        cursor2.close()
        cursor.close()
        cnx.close()

        # Voltar para a página inicial
        return redirect("/")
    
    # Caso seja GET, buscar os dados do utilizador
    cursor.execute("SELECT id, nome, email FROM utilizadores WHERE id = %s", (id,))
    utilizador = cursor.fetchone()

    # Fechar conexões
    cursor.close()
    cnx.close()

    # Enviar dados para o formulário já preenchido
    return render_template("form.html", titulo="Editar utilizador", utilizador=utilizador)


# ---------------------------------------------------
# Rota para apagar utilizador
# ---------------------------------------------------
@app.route("/apagar/<int:id>", methods=["POST"])
def deleta_utilizador(id):

    # Conectar ao banco
    cnx = ligar_bd()
    cursor = cnx.cursor()

    # Apagar utilizador pelo ID
    cursor.execute("DELETE FROM utilizadores WHERE id = %s", (id,))    
    cnx.commit()

    # Encerrar conexão
    cursor.close()
    cnx.close()

    # Voltar à página principal
    return redirect("/")
    

# ---------------------------------------------------
# Iniciar o servidor Flask
# ---------------------------------------------------
app.run(debug=True)
