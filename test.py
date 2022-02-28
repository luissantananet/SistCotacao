from PyQt5 import uic, QtWidgets
import mysql.connector
import pandas as pd
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cofggcvf",
    database="cotacao"
)

cursor = banco.cursor()
cursor.execute("SELECT * FROM tarifas_minimas") 
tarifas_minimas = cursor.fetchall()
valor_id = tarifas_minimas[0][0]
#descs20 = tarifas_minimas[0][2]
print(valor_id)