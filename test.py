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
cursor3 = banco.cursor()
cursor3.execute("SELECT id FROM cubagem")
dados_lido = cursor3.fetchall()
banco.commit()

print(dados_lido)
