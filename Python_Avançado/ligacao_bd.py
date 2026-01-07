# Instalar biblioteca -- python -m 
# pip3 install mysql-connector-python

import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(host = "62.28.39.135", user = "efa0125", password = "123.Abc", database = "efa0125_25_formacao_crud")
    print("Ligação deu certo!")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("As credenciais são inválidas.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("A base de dados não existe.")
    else: 
        print(err)
else: 
    cnx.close()