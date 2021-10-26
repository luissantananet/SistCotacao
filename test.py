from PyQt5 import uic, QtWidgets
import mysql.connector
import pandas as pd
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cofggcvf",
    database="cotacao"
)

tabela = pd.read_excel('cidades.xls')
#print(tabela)




"""for i in range(0,5570):
    cidades = (tabela['cidade']) #= input(str(tabela.cols['cidade']))
    uf=(tabela['UF'])"""

for i in range(0,5570):
    cidades = (tabela['cidade']) #= input(str(tabela.cols['cidade']))
    uf=(tabela['UF'])
    cursor = banco.cursor()
    comando_SQL = "INSERT INTO cidades (cidade, uf) VALUES (%s,%s)"
    dados = (str(cidades), str(uf))
    #tarifas = cursor.fetchall()
    cursor.execute(comando_SQL,dados)
    cursor.close()