from inspect import trace
from pickle import TRUE
from unittest import result
from PyQt5 import uic, QtWidgets
import mysql.connector
import pandas as pd
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cofggcvf",
    database="cotacao"
)

dim1 = 1.2
dim2 = 3.5
dim3 = 4.0
vol = 1
resultado = 50.50

dados = {dim1, dim2 ,dim3,vol,resultado}

cursor2 = banco.cursor()
comando_SQL = "SELECT * FROM cubagem"
cursor2.execute(comando_SQL)
dados_lidos = cursor2.fetchall()
for i in range(0, len(dados)):
    for j in range(0, 5):
        cursor = banco.cursor()
        #comando_sql=("INSERT INTO cubagem(dim1,dim2,dim3,volume,m3) VALUES('{}')".format( float(dados[i][j])))
        #dado=(float(dados)
        cursor.execute("INSERT INTO cubagem(dim1,dim2,dim3,volume,m3) VALUES('{}','{}','{}','{}','{}')".format(float(dados[i][j])))
        banco.commit() 

print(dados)
print(type(dados))
print(dados_lidos)