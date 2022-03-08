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
cursor2 = banco.cursor()
cursor2.execute("SELECT id FROM tarifas")
tarifas = cursor2.fetchall()
total_id = len(tarifas)
ids= tarifas

print(total_id)
print(type(total_id))
print(ids)
print(type(ids))
idtb='TB'
idtbl="TBL"
if ids == [] or ids != idtb:
    print('teste ok')
else:
    print('teste error')