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
rem_cnpj = '4616532000172'
cursor = banco.cursor()
cursor.execute("SELECT * FROM cliente WHERE id="+ str(rem_cnpj))
dados_lidos = cursor.fetchall()
cliente_cnpj = dados_lidos

print(cliente_cnpj)