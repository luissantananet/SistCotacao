from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
import mysql.connector.errors

# Conexão com o bando de dados MySQL
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cofggcvf",
    database="cotacao"
)
def calc_contacao():
    valornf=frm_principal.edt_valor_merc.text()
    fcif=frm_principal.edt_frete_cif.text()
    ffob=frm_principal.edt_frete_fob.text()
    flit=frm_principal.edt_frete_litoral.text()
    valor_nf=frm_principal.edt_valor_merc.text()
    peso=frm_principal.edt_peso.text()

    if peso != " ":
        # Peso=frm_principal.edt_peso.text()
        fpesores = float(peso) * 0.52
        frm_principal.edt_fpeso.setText(str('%.2f'%fpesores))
    
    if valornf != " ":
        # Valor GRIS
        valorgris = float(valornf) * 0.0025 #/0.88+1.92
        frm_principal.edt_gris.setText(str('%.2f'%valorgris)) 
        # Valor Ad_Valoren
        vaload = float(valornf) * 0.005
        frm_principal.edt_ad.setText(str('%.2f'%vaload))
        # Valor pedagio
        valorped = float(peso)/100 * 3.04
        frm_principal.edt_pedag.setText(str('%.2f'%valorped))
        # Valor taxa 
        valortaxa = float(valorped) + 36.68
        frm_principal.edt_taxas.setText(str('%.2f'%valortaxa))
        # Valor do ICMS
        icmsres = (float(valornf)/0.88)-float(valornf)
        frm_principal.edt_icms.setText(str('%.2f'%icmsres))
    # Valor frete cif
    valorcif = float(fpesores) + float(valorgris) + float(vaload) + float(valortaxa)
    frm_principal.edt_frete_cif.setText(str('%.2f'%valorcif))
    # Valor frete fob
    valorfob = float(valorcif) / 0.88
    frm_principal.edt_frete_fob.setText(str('%.2f'%valorfob))
    # Valor frete litoral
    valorlitoral = float(valorfob) / 0.69
    frm_principal.edt_frete_litoral.setText(str('%.2f'%valorlitoral))
def salva_cotacao():
    pass
def limpar_tela():
    pass
def add_m3():
    pass
def pesquisa_cliente():
    pass
def chama_tarifa():
    cursor4 = banco.cursor()
    cursor4.execute("SELECT * FROM tarifas_minimas") 
    tabelas = cursor4.fetchall()
    frm_tarifa.edt_base_20.setText(str(tabelas[0][2]))
    frm_tarifa.edt_base_lit_20.setText(str(tabelas[0][3]))
    frm_tarifa.edt_ad_gris_20.setText(str(tabelas[0][4]))
    frm_tarifa.edt_pedagio_20.setText(str(tabelas[0][5]))

    cursor2 = banco.cursor()
    cursor2.execute("SELECT * FROM tarifas") 
    taxas = cursor2.fetchall()
        
    frm_tarifa.edt_fpeso.setText(str(taxas[0][1]))
    frm_tarifa.edt_ad.setText(str(taxas[0][2]))
    frm_tarifa.edt_gris.setText(str(taxas[0][3]))
    frm_tarifa.edt_taxa.setText(str(taxas[0][4]))
    frm_tarifa.edt_icms.setText(str(taxas[0][5]))

    frm_tarifa.show()

def salva_tarifa():
    desc20 = frm_tarifa.desc_20.text()
    tBase20 = frm_tarifa.edt_base_20.text()
    tLit20 = frm_tarifa.edt_base_lit_20.text()
    ad_gris20 = frm_tarifa.edt_ad_gris_20.text()
    ped20 = frm_tarifa.edt_pedagio_20.text()
    
    desc50 = frm_tarifa.desc_50.text()
    tBase50 = frm_tarifa.edt_base_50.text()
    tLit50 = frm_tarifa.edt_base_lit_50.text()
    ad_gris50 = frm_tarifa.edt_ad_gris_50.text()
    ped50 = frm_tarifa.edt_pedagio_50.text()
    

    desc100 = frm_tarifa.desc_100.text()
    tBase100 = frm_tarifa.edt_base_100.text()
    tLit100 = frm_tarifa.edt_base_lit_100.text()
    ad_gris100 = frm_tarifa.edt_ad_gris_100.text()
    ped100 = frm_tarifa.edt_pedagio_100.text()

    desc150 = frm_tarifa.desc_150.text()
    tBase150 = frm_tarifa.edt_base_150.text()
    tLit150 = frm_tarifa.edt_base_lit_150.text()
    ad_gris150 = frm_tarifa.edt_ad_gris_150.text()
    ped150 = frm_tarifa.edt_pedagio_150.text()

    desc200 = frm_tarifa.desc_200.text()
    tBase200 = frm_tarifa.edt_base_200.text()
    tLit200 = frm_tarifa.edt_base_lit_200.text()
    ad_gris200 = frm_tarifa.edt_ad_gris_200.text()
    ped200 = frm_tarifa.edt_pedagio_200.text()
    
    desc250 = frm_tarifa.desc_250.text()
    tBase250 = frm_tarifa.edt_base_250.text()
    tLit250 = frm_tarifa.edt_base_lit_250.text()
    ad_gris250 = frm_tarifa.edt_ad_gris_250.text()
    ped250 = frm_tarifa.edt_pedagio_250.text()
    
    desc300 = frm_tarifa.desc_300.text()
    tBase300 = frm_tarifa.edt_base_300.text()
    tLit300 = frm_tarifa.edt_base_lit_300.text()
    ad_gris300 = frm_tarifa.edt_ad_gris_300.text()
    ped300 = frm_tarifa.edt_pedagio_300.text()

    cursor2 = banco.cursor()
    cursor2.execute("SELECT * FROM tarifas_minimas") # WHERE id="+str(1)
    dados = cursor2.fetchall()
    tabela = dados[0][1]
    
    if desc20 == tabela:
        ids =  tabela = dados[0][0]
        cursor = banco.cursor()
        cursor.execute("UPDATE tarifas_minimas SET tarifa_base='{}',tarifa_litoral='{}',ad_Gris='{}',pedagio='{}',id='{}'".format(tBase20,tLit20,ad_gris20,ped20,ids))
        banco.commit()
        QMessageBox.information(frm_tarifa, "Aviso", "tabela cadastradas")
    if desc50 == "De 21 até 50Kg":
        pass
    if desc100 != "De 51 até 100Kg":
        pass
    if desc150 != "De 101 até 150Kg":
        pass
    if desc200 != "De 151 até 200Kg":
        pass
    if desc250 != "De 201 até 250Kg":
        pass
    if desc300 != "De 251 até 300Kg":
        pass

def salva_taxa():
    fPeso = frm_tarifa.edt_fpeso.text()
    ad_v = frm_tarifa.edt_ad.text()
    gris = frm_tarifa.edt_gris.text()
    taxa = frm_tarifa.edt_taxa.text()
    icms = frm_tarifa.edt_icms.text()
    cursor2 = banco.cursor()
    cursor2.execute("SELECT * FROM tarifas") # WHERE id="+str(1)
    tarifas = cursor2.fetchall()
    valor_id2 = len(tarifas)
    frm_tarifa.show()
    if valor_id2 == 0:
        cursor = banco.cursor()
        comando_sql=("INSERT INTO tarifas(frete_peso,ad_valoren,gris,taxa,icms) VALUES(%s,%s,%s,%s,%s)")
        dados=(float(fPeso),float(ad_v),float(gris),float(taxa),float(icms))
        cursor.execute(comando_sql,dados)
        banco.commit()
        QMessageBox.information(frm_tarifa, "Aviso", "Taxas cadastradas")
    else:
        cursor = banco.cursor()
        cursor.execute("UPDATE tarifas SET frete_peso='{}',ad_valoren='{}',gris='{}',taxa='{}',icms='{}',id='{}'".format(fPeso,ad_v,gris,taxa,icms,valor_id2))
        banco.commit()
        QMessageBox.information(frm_tarifa, "Aviso", "Taxas Atualizadas")
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    frm_principal = uic.loadUi('frm_principal_full.ui')
    frm_tarifa = uic.loadUi('frm_tarifa.ui')

    #botões da tela principal
    frm_principal.btn_calcula.clicked.connect(calc_contacao)
    frm_principal.btn_salvar.clicked.connect(salva_cotacao)
    frm_principal.btn_limpa.clicked.connect(limpar_tela)
    frm_principal.btn_adicionar.clicked.connect(add_m3)
    frm_principal.btn_rem_pesq.clicked.connect(pesquisa_cliente)
    frm_principal.btn_dest_pesq.clicked.connect(pesquisa_cliente)
    frm_principal.btn_tarifa.clicked.connect(chama_tarifa)
    #botões da tela tarifas
    frm_tarifa.btn_salvar_taxa.clicked.connect(salva_taxa)
    frm_tarifa.btn_salvar_tabela.clicked.connect(salva_tarifa)
    frm_principal.show()
    app.exec()