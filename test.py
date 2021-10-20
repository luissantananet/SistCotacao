import mysql.connector
from PyQt5 import uic, QtWidgets

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cofggcvf",
    database="cotacao"
)
"""valornf = 100

def valo_gris_100():
    valorgris_100 = valornf * 0.0015/0.88+1.92
    valor = ('%.2f' % (valorgris_100))
    return valor

print(type(valo_gris_100()))
print(valo_gris_100())
"""

"""cursor = banco.cursor()
cursor.execute("SELECT id FROM tarifas_minimas")
dados_lidos = cursor.fetchall()
valor_id = dados_lidos[1][0]
for i in range(valor_id):
    print(valor_id)
print (valor_id)"""

cursor = banco.cursor()
cursor.execute("SELECT * FROM tarifas_minimas WHERE id="+str(2))
tarifas_minimas = cursor.fetchall()
for I in tarifas_minimas:
    print(tarifas_minimas[0][0])

