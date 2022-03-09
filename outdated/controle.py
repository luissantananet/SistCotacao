from PyQt5 import uic, QtWidgets
import mysql.connector
import pandas as pd
cidades = pd.read_excel(r"C:\Users\usuario\Documents\GitHub\SistCotacao\cidades.xls")

"""valornf = 100"""
numero_id = 0
# Conexão com o bando de dados MySQL
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cofggcvf",
    database="cotacao"
)

# Calcular da contação
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
        valorgris = float(valornf) * 0.0015 #/0.88+1.92
        frm_principal.edt_gris.setText(str('%.2f'%valorgris)) 
        # Valor Ad_Valoren
        vaload = float(valornf) * 0.004
        frm_principal.edt_ad.setText(str('%.2f'%vaload))
        # Valor pedagio
        valorped = float(peso)/100 * 1.92
        frm_principal.edt_pedag.setText(str('%.2f'%valorped))
        # Valor taxa 
        valortaxa = float(valorped) + 32.45
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
# Salva registro de cotação
def salva_cotacao():
    emit_cnpj = frm_principal.edt_cnpj_emit.text()
    emit_nome = frm_principal.edt_nome_emit.text()
    dest_cnpj = frm_principal.edt_cnpj_dest.text()
    dest_nome = frm_principal.edt_nome_dest.text()
    edt_peso = frm_principal.edt_peso.text
    tipo_merc = frm_principal.edit_tipo_merc.text()
    edit_peso_cubo = frm_principal.edit_peso_cubo.text()
    quant = frm_principal.edt_volume.text()
    valornf=frm_principal.edt_valor_merc.text()
    fpeso=frm_principal.edt_fpeso.text()
    edt_total_m3 = frm_principal.edt_total_m3.text()
    pedagio=frm_principal.edt_pedag.text()
    ad=frm_principal.edt_ad.text()
    gris=frm_principal.edt_gris.text()
    taxa=frm_principal.edt_taxas.text()
    icms=frm_principal.edt_icms.text()
    fcif=frm_principal.edt_frete_cif.text()
    ffob=frm_principal.edt_frete_fob.text()
    flit=frm_principal.edt_frete_litoral.text()
    comb_cid_emit = frm_principal.edt_cidade_emit.text()
    comb_uf_emit = frm_principal.edt_estado_emit.text()
    comb_cid_dest = frm_principal.edt_cidade_dest.text()
    comb_uf_dest = frm_principal.edt_estado_dest.text()
    dim1 = frm_principal.edt_dim1.text()
    dim2 = frm_principal.edt_dim2.text()
    dim3 = frm_principal.edt_dim3.text()
    vol = frm_principal.edit_vol.text()
    resultado_m3 = frm_principal.edit_resultado_m3.text()
    cif_fob = ""
    if frm_principal.rbtn_cif.isChecked():
        cif_fob = "Cif"
    elif frm_principal.rbtn_fob.isChecked():
        cif_fob = "Fob"
    cursor = banco.cursor()
    comando_SQL = "CALL salvar_cotacao(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(fpeso),str(pedagio),str(ad),str(gris),str(taxa),str(icms),str(fcif),str(ffob),str(flit),
        str(dim1),str(dim2),str(dim3),str(vol),str(resultado_m3),
        str(emit_cnpj),str(emit_nome),str(dest_cnpj),str(dest_nome),str(comb_cid_emit),str(comb_uf_emit),str(comb_cid_dest),str(comb_uf_dest),str(cif_fob),str(valornf),str(edt_peso),str(quant),str(tipo_merc),str(edit_peso_cubo),str(edt_total_m3))
    cursor.execute(comando_SQL,dados)
    cursor.close()
# Carlular tarifas padrôes #no futuro
def calc_tarifa20():
    base=frm_tarifa.edt_base_20.text()
    gris20=frm_tarifa.edt_gris_20.text()
    fretefinal=frm_tarifa.edt_ffinal_20.text()
    ad=frm_tarifa.edt_ad_20.text()
    fretetotal=frm_tarifa.edt_ftotal_20.text()
    fretelitoral=frm_tarifa.edt_litoral_20.text()
    
    
    #calcular frente
# Carlular tarifas padrôes #no futuro
def salva_tarifaM():
    pass
# Chama tela de tarifas padôes #no futuro
def chama_tarifa():
    frm_tarifa.show()
# Calcular tarifas e frente #no futuro
def chama_tarifas_minimas():
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
        frm_tarifa_edit.edt_litoral_50.setText(str(tarifas_minimas[0][7]))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    frm_principal= uic.loadUi('frm_principal.ui')
    # botões da tela principal
    frm_principal.btn_tarifa.clicked.connect(chama_tarifas_minimas)
    frm_principal.btn_calcula.clicked.connect(calc_contacao)
    frm_principal.btn_salvar.clicked.connect(salva_cotacao)
    """frm_principal.comboBox_cidade_emit.addItems(cidades['Município'])
    frm_principal.comboBox_estado_emit.addItems(cidades['UF'])
    frm_principal.comboBox_cidade_dest.addItems(cidades['Município'])
    frm_principal.comboBox_estado_dest.addItems(cidades['UF'])"""
    # botões da tela tarifa
    frm_tarifa = uic.loadUi('frm_tarifa.ui')
    frm_tarifa_edit = uic.loadUi('frm_tarifa_edit.ui') 

    frm_principal.show()
    app.exec()


"""# Aqui vai para tela de editar cotação#
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