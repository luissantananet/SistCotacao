from PyQt5 import uic, QtWidgets
import mysql.connector
import pandas as pd
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cofggcvf",
    database="cotacao"
)

cursor2 = banco.cursor()
cursor2.execute("SELECT * FROM tarifas") # WHERE id="+str(1)
dados_lidos = cursor2.fetchall()
#valor_id = dados_lidos[0][0]


print(len(dados_lidos))