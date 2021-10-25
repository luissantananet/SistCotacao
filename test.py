from PyQt5 import uic, QtWidgets
import mysql.connector
import pandas as pd
"""banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cofggcvf",
    database="cotacao"
)"""



x = pd.read_excel(r"C:\Users\usuario\Documents\GitHub\SistCotacao\cidades.xls")

cidades = []
uf = []

for i in range(0,len(x)):
    
    cidades = x['cidade']
    uf = x['UF']
        

print('-='*30)
print(cidades)
print('-='*30)
print(uf)
print('-='*30)



"""for i in range(len(x)):
    for j in range(len(x)):
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO cidades (cidade, uf) VALUES (%s,%s,%s,%s)"
        dados = (str(cidades), str(uf))
        tarifas = cursor.fetchall()
        cursor.execute(comando_SQL,dados)

"""




#print(x['Município'][3],['UF'][3])
#print(x)



"""for i in range(0,len(x)):
    for j in range(0,len(x)):
        lista[i][j] = input(f"{x['Município']},{x['UF']}")
print('-='*30)
for l in range(0,len(lista)):
    for c in range(0,len(lista)):
        print(lista[l][c], end='')
    print()
print('-='*30)"""