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
cursor = banco.cursor()
cursor.execute("SELECT * FROM cliente")
cliente = cursor.fetchall()

print(cliente)
