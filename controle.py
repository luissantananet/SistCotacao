from PyQt5 import uic, QtWidgets
import mysql.connector

valornf = 100
numero_id = 0

"""banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cofggcvf",
    database="cotacao"
)"""

#calcular da contação
def calc_contacao():
    valornf=frm_principal.edt_valor_merc.text()
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

    if peso != " ":
        #peso=frm_principal.edt_peso.text()
        fpesores = float(peso) * 0.52
        frm_principal.edt_fpeso.setText(str('%.2f'%fpesores))
    
    if valornf != " ":
        #valor GRIS
        valorgris = float(valornf) * 0.0015 #/0.88+1.92
        frm_principal.edt_gris.setText(str('%.2f'%valorgris)) 
        #valor Ad_Valoren
        vaload = float(valornf) * 0.004
        frm_principal.edt_ad.setText(str('%.2f'%vaload))
        #valor pedagio
        valorped = float(peso)/100 * 1.92
        frm_principal.edt_pedag.setText(str('%.2f'%valorped))
        #valor taxa 
        valortaxa = float(valorped) + 32.45
        frm_principal.edt_taxas.setText(str('%.2f'%valortaxa))
    

    
def calc_trarifa20():
    base=frm_tarifa.edt_base_20.text()
    gris20=frm_tarifa.edt_gris_20.text()
    fretefinal=frm_tarifa.edt_ffinal_20.text()
    ad=frm_tarifa.edt_ad_20.text()
    fretetotal=frm_tarifa.edt_ftotal_20.text()
    fretelitoral=frm_tarifa.edt_litoral_20.text()
    
    #calcular frente

def salva_tarifaM():
    pass

def chama_tarifa():
    frm_tarifa.show()
"""def chama_tarifas_minimas():
    global numero_id

    cursor = banco.cursor()
    cursor.execute("SELECT * FROM tarifas_minimas") # WHERE id="+str(1)
    tarifas_minimas = cursor.fetchall()
    valor_id = tarifas_minimas[0][0]
    frm_tarifa_edit.show()
    print(valor_id)
    if valor_id == 1:
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM tarifas_minimas WHERE id="+str(1)) # WHERE id="+str(1)
        tarifas_minimas = cursor.fetchall()
        frm_tarifa_edit.edt_base_20.setText(str(tarifas_minimas[0][2]))
        frm_tarifa_edit.edt_gris_20.setText(str(tarifas_minimas[0][3]))  
        frm_tarifa_edit.edt_ffinal_20.setText(str(tarifas_minimas[0][4]))  
        frm_tarifa_edit.edt_ad_20.setText(str(tarifas_minimas[0][5]))  
        frm_tarifa_edit.edt_ftotal_20.setText(str(tarifas_minimas[0][6]))
        frm_tarifa_edit.edt_litoral_20.setText(str(tarifas_minimas[0][7]))
    elif  valor_id == 2:
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM tarifas_minimas WHERE id="+str(2)) # WHERE id="+str(1)
        tarifas_minimas = cursor.fetchall()
        frm_tarifa_edit.edt_base_50.setText(str(tarifas_minimas[0][2]))
        frm_tarifa_edit.edt_gris_50.setText(str(tarifas_minimas[0][3]))  
        frm_tarifa_edit.edt_ffinal_50.setText(str(tarifas_minimas[0][4]))  
        frm_tarifa_edit.edt_ad_50.setText(str(tarifas_minimas[0][5]))  
        frm_tarifa_edit.edt_ftotal_50.setText(str(tarifas_minimas[0][6]))
        frm_tarifa_edit.edt_litoral_50.setText(str(tarifas_minimas[0][7]))"""
    

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    frm_principal= uic.loadUi('frm_principal.ui')
    # botões da tela principal
    frm_principal.btn_tarifa.clicked.connect()#chama_tarifas_minimas#)
    frm_principal.btn_calcula.clicked.connect(calc_contacao)
    # botões da tela tarifa
    frm_tarifa = uic.loadUi('frm_tarifa.ui')
    frm_tarifa_edit = uic.loadUi('frm_tarifa_edit.ui')

    """cursor = banco.cursor()
    cursor.execute("SELECT * FROM tarifa") # WHERE id="+str(1)
    tarifas = cursor.fetchall()
    valor_id = tarifas[0][0]
    
    #print(valor_id)
    
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM tarifa WHERE id="+str(1)) # WHERE id="+str(1)
    tarifas = cursor.fetchall()
    frm_principal.edt_fpeso.setText(str(tarifas[0][1]))
    frm_principal.edt_pedag.setText(str(tarifas[0][2]))
    frm_principal.edt_ad.setText(str(tarifas[0][3]))  
    frm_principal.edt_gris.setText(str(tarifas[0][4]))  
    frm_principal.edt_taxas.setText(str(tarifas[0][5]))  
    frm_principal.edt_icms.setText(str(tarifas[0][6]))
    frm_principal.edt_frete_cif.setText(str(tarifas[0][7]))
    frm_principal.edt_frete_fob.setText(str(tarifas[0][8]))
    frm_principal.edt_frete_litoral.setText(str(tarifas[0][9]))"""

    frm_principal.show()
    app.exec()