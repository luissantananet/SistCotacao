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
totalpreso = 2.400
totalm3 = 3

cursor2 = banco.cursor()
cursor2.execute("SELECT id FROM cubagem")
dados_id= cursor2.fetchall()
valor_id = dados_id
for dados in range(0, len(dados_id)):
    ids = dados_id[dados][0]

cursor2 = banco.cursor()
cursor2.execute("SELECT * FROM cubagem")
dados_lidos = cursor2.fetchall()
totalm3lista = 0 
for dados_lido in range(len(dados_lidos)):
    lista = float(dados_lidos[dados_lido][5])
    
    totalm3lista = float(totalm3lista + lista)


print('------------')
print('lista',lista)
print(type(lista))
print('------------')
print('totalm3lista',totalm3lista)
print(len(dados_lidos))
