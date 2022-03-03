from inspect import trace
from pickle import TRUE
from PyQt5 import uic, QtWidgets
import mysql.connector
import pandas as pd
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cofggcvf",
    database="cotacao"
)
global numero_id
"""cursor = banco.cursor()
cursor.execute("SELECT * FROM tarifas_minimas") 
tarifas_minimas = cursor.fetchall()
#valor_id = tarifas_minimas[0][0]
desc = tarifas_minimas[2][1]
#descs20 = tarifas_minimas[0][2]
print(desc)"""
cursor2 = banco.cursor()
cursor2.execute("SELECT id FROM tarifas_minimas")
dadosid = cursor2.fetchall()

cursor2 = banco.cursor()
cursor2.execute("SELECT * FROM tarifas_minimas") 
dados = cursor2.fetchall()
numero_id = dadosid[2][0]

print(dados[2])