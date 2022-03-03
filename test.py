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
cursor2.execute("SELECT * FROM tarifas")
taxas = cursor2.fetchall()

cursor2 = banco.cursor()
cursor2.execute("SELECT * FROM tarifas_minimas") 
tabelas = cursor2.fetchall()

dadoslidos=float(taxas[0][1])
tabelas_ped = float(tabelas[0][5])
print(tabelas[0][3])
peso = 10

teste = tabelas_ped *float(peso) / 100 
print(teste)