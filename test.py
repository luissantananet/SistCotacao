from PyQt5 import uic, QtWidgets
import mysql.connector
import pandas as pd


x = pd.read_excel(r"C:\Users\usuario\Documents\GitHub\SistCotacao\cidades.xls")

#print(x['Município'][3],['UF'][3])
#print(x)


list=[[0,0]]
for i in range(len(x)):
    for j in range(len(x)):
        lista = (f"{i}{j}{x['Município']},{x['UF']}")

    print(lista)
print(len(x))