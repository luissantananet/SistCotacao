from PyQt5 import uic, QtWidgets
import mysql.connector
import pandas as pd


x = pd.read_excel("cidades.xls")
y =x
print(x)
print(type(x))
print(type(y))