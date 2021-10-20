from logging import NullHandler
import mysql.connector
from PyQt5 import uic, QtWidgets


def valo_peso():
    peso=frm_principal.edt_peso.text()
    fpesores =peso * 0.52
    return str(fpesores)
print(type(valo_peso))

"""banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cofggcvf",
    database="cotacao"
)
valornf = 100

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
print (valor_id)

cursor = banco.cursor()
cursor.execute("SELECT * FROM tarifas_minimas WHERE id="+str(2))
tarifas_minimas = cursor.fetchall()
for I in tarifas_minimas:
    print(tarifas_minimas[0][0])"""

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    frm_principal= uic.loadUi('frm_principal.ui')
    # botões da tela principal
    #frm_principal.btn_tarifa.clicked.connect()
    # botões da tela tarifa
    frm_tarifa = uic.loadUi('frm_tarifa.ui')
    frm_tarifa_edit = uic.loadUi('frm_tarifa_edit.ui')

    fpeso=frm_principal.edt_fpeso.text()
    pedagio=frm_principal.edt_pedag.text()
    ad=frm_principal.edt_ad.text()
    gris=frm_principal.edt_gris.text()
    taxa=frm_principal.edt_taxas.text()
    icms=frm_principal.edt_icms.text()
    fcif=frm_principal.edt_frete_cif.text()
    ffob=frm_principal.edt_frete_fob.text()
    flit=frm_principal.edt_frete_litoral.text()
    valor_nf=frm_principal.edt_valor_merc.text()
    peso=frm_principal.edt_peso.text()
    while True:
        
        if str(peso) != "":
            peso=frm_principal.edt_peso.text()
            fpesores =peso * 0.52
            print(type(fpesores))
            print(fpesores)
            frm_principal.edt_fpeso.setText(str(fpesores))
        else:
            break
    
    frm_principal.show()
    app.exec()