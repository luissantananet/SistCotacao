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

cursor2 = banco.cursor()
cursor2.execute("SELECT * FROM tarifas_minimas")
tabelas = cursor2.fetchall()

valornf = 250

adg20 = float(tabelas[0][4])
print(adg20)
fb20 = float(tabelas[0][2])
print('fbase ',fb20)
fbl20 = float(tabelas[0][3])
print('fbase_litoral ',fbl20)
ad_g20 = float(valornf) * adg20
print('ad_gris ',ad_g20)
ped20 = float(tabelas[0][5])
print('pedagio ',ped20)
pedl20 = float( tabelas[0][6])
print(pedl20)
ftotal_20 = fb20 + ped20 + ad_g20
ftotall_20 = float(fbl20 + pedl20 + ad_g20)
print("***********************************")
print(ftotal_20)
print("***********************************")
print(ftotall_20)
print("***********************************")