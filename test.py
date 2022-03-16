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
cursor2 = banco.cursor()
cursor2.execute("SELECT * FROM cubagem")
dados_lidos = cursor2.fetchall()
lista = dados_lidos[0][5]
#valor_id = dados_lidos[0][0]

print(lista)