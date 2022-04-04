
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem
import mysql.connector
import mysql.connector.errors
import datetime
from reportlab.pdfgen import canvas

# Conexão com o bando de dados MySQL
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cofggcvf",
    database="cotacao"
)
numero_id = 0
cliente_id = 0
cliente_cnpj = 0
id_m3 = 0
result_peso_m3 = 0
client = 0

def calc_contacao():
    # Acesso as Taxas e tabelas fixas no banco de dados
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM tarifas")
    taxas = cursor.fetchall()
    cursor2 = banco.cursor()
    cursor2.execute("SELECT * FROM tarifas_minimas") 
    tabelas = cursor2.fetchall()
    # TAXAS BASE PADRÃO
    taxa_fpeso = float(taxas[0][2])
    taxa_ad = float(taxas[0][3])
    taxa_gris = float(taxas[0][4])
    taxa_taxas = float(taxas[0][5])
    taxa_icms = float(taxas[0][6])
    # TAXAS LITORAL/SERRA
    taxa_fpesol = float(taxas[1][2])
    taxa_adl = float(taxas[1][3])
    taxa_grisl = float(taxas[1][4])
    taxa_taxasl = float(taxas[1][5])
    taxa_icmsl = float(taxas[1][6])
    tabelas_ped = float(tabelas[0][5])
    # Tabelas
    valornf=frm_principal.edt_valor_merc.text().replace(',','.')
    peso=frm_principal.edt_peso.text().replace(',','.')
    peso_m3 = frm_principal.edit_peso_cubo.text().replace(',','.')
    if valornf != "" or peso != "":
        if peso != "":
            if peso_m3 != '':
                if float(peso) > float(peso_m3):
                    fpesores = float(peso) * taxa_fpeso #0.52
                    frm_principal.edt_fpeso.setText(str('%.2f'%fpesores).replace('.',','))
                else:
                    fpesores = float(peso_m3) * taxa_fpeso #0.52
                    frm_principal.edt_fpeso.setText(str('%.2f'%fpesores).replace('.',','))
            else:
                fpesores = float(peso) * taxa_fpeso #0.52
                frm_principal.edt_fpeso.setText(str('%.2f'%fpesores).replace('.',','))
        else:
            QMessageBox.about(frm_principal, "Aviso", "Insira o Peso!")
            frm_principal.show()
        if valornf != "":
            # Valor GRIS
            valorgris = float(valornf) * taxa_gris #0.0025 #/0.88+1.92
            frm_principal.edt_gris.setText(str('%.2f'%valorgris).replace('.',',')) 
            # Valor Ad_Valoren
            vaload = float(valornf) * taxa_ad #0.005
            frm_principal.edt_ad.setText(str('%.2f'%vaload).replace('.',','))
            # Valor pedagio
            if peso != "":
                valorped = float(tabelas_ped) *float(peso) / 100 #3.04
                frm_principal.edt_pedag.setText(str('%.2f'%valorped).replace('.',','))
                # Valor taxa 
                valortaxa = float(valorped) + taxa_taxas #36.68
                frm_principal.edt_taxas.setText(str('%.2f'%valortaxa).replace('.',','))
                # Valor frete cif
                valorcif = float(fpesores) + float(valorgris) + float(vaload) + float(valortaxa)
                frm_principal.edt_frete_cif.setText(str('%.2f'%valorcif).replace('.',','))
                valorfob = float(valorcif) / taxa_icms #0.88
                frm_principal.edt_frete_fob.setText(str('%.2f'%valorfob).replace('.',','))
                # Valor frete litoral
                fpresol = float(peso) * taxa_fpesol
                valorgrisl = float(valornf) * taxa_grisl
                valoadl = float(valornf) * taxa_adl
                valortaxal = float(valorped) + taxa_taxasl
                valorlitoral = float(fpresol) + float(valorgrisl) + float(valoadl) + float(valortaxal) + float(taxa_icmsl)
                frm_principal.edt_frete_litoral.setText(str('%.2f'%valorlitoral).replace('.',','))
                # Calculo da tabelas
                adg20 = float(tabelas[0][4])
                fb20 = float(tabelas[0][2])
                fbl20 = float(tabelas[0][3])
                ad_g20 = float(valornf) * adg20
                ped20 = float(tabelas[0][5])
                pedl20 = float( tabelas[0][6])
                ftotal_20 = fb20 + ped20 + ad_g20
                ftotall_20 = float(fbl20 + pedl20 + ad_g20)
                frm_principal.edt_ftotal_20.setText(str('%.2f'%ftotal_20).replace('.',','))
                frm_principal.edt_litoral_20.setText(str('%.2f'%ftotall_20).replace('.',','))

                adg50 = float(tabelas[1][4])
                fb50 = float(tabelas[1][2])
                fbl50 = float(tabelas[1][3])
                ad_g50 = float(valornf) * adg50
                ped50 = float(tabelas[1][5])
                pedl50 = float( tabelas[1][6])
                ftotal_50 = fb50 + ped50 + ad_g50
                ftotall_50 = float(fbl50 + pedl50 + ad_g50)
                frm_principal.edt_ftotal_50.setText(str('%.2f'%ftotal_50).replace('.',','))
                frm_principal.edt_litoral_50.setText(str('%.2f'%ftotall_50).replace('.',','))

                adg100 = float(tabelas[2][4])
                fb100 = float(tabelas[2][2])
                fbl100 = float(tabelas[2][3])
                ad_g100 = float(valornf) * adg100
                ped100 = float(tabelas[2][5])
                pedl100 = float( tabelas[2][6])
                ftotal_100 = fb100 + ped100 + ad_g100
                ftotall_100 = fbl100 + pedl100 + ad_g100
                frm_principal.edt_ftotal_100.setText(str('%.2f'%ftotal_100).replace('.',','))
                frm_principal.edt_litoral_100.setText(str('%.2f'%ftotall_100).replace('.',','))

                adg150 = float(tabelas[3][4])
                fb150 = float(tabelas[3][2])
                fbl150 = float(tabelas[3][3])
                ad_g150 = float(valornf) * adg150
                ped150 = float(tabelas[3][5])
                pedl150 = float( tabelas[3][6])
                ftotal_150 = fb150 + ped150 + ad_g150
                ftotall_150 = float(fbl150 + pedl150 + ad_g150)
                frm_principal.edt_ftotal_150.setText(str('%.2f'%ftotal_150).replace('.',','))
                frm_principal.edt_litoral_150.setText(str('%.2f'%ftotall_150).replace('.',','))

                adg200 = float(tabelas[4][4])
                fb200 = float(tabelas[4][2])
                fbl200 = float(tabelas[4][3])
                ad_g200 = float(valornf) * adg200
                ped200 = float(tabelas[4][5])
                pedl200 = float( tabelas[4][6])
                ftotal_200 = fb200 + ped200 + ad_g200
                ftotall_200 = float(fbl200 + pedl200 + ad_g200)
                frm_principal.edt_ftotal_200.setText(str('%.2f'%ftotal_200).replace('.',','))
                frm_principal.edt_litoral_200.setText(str('%.2f'%ftotall_200).replace('.',','))

                adg250 = float(tabelas[5][4])
                fb250 = float(tabelas[5][2])
                fbl250 = float(tabelas[5][3])
                ad_g250 = float(valornf) * adg250
                ped250 = float(tabelas[5][5])
                pedl250 = float( tabelas[5][6])
                ftotal_250 = fb250 + ped250 + ad_g250
                ftotall_250 = float(fbl250 + pedl250 + ad_g250)
                frm_principal.edt_ftotal_250.setText(str('%.2f'%ftotal_250).replace('.',','))
                frm_principal.edt_litoral_250.setText(str('%.2f'%ftotall_250).replace('.',','))

                adg300 = float(tabelas[6][4])
                fb300 = float(tabelas[6][2])
                fbl300 = float(tabelas[6][3])
                ad_g300 = float(valornf) * adg300
                ped300 = float(tabelas[6][5])
                pedl300 = float( tabelas[6][6])
                ftotal_300 = fb300 + ped300 + ad_g300
                ftotall_300 = float(fbl300 + pedl300 + ad_g300)
                frm_principal.edt_ftotal_300.setText(str('%.2f'%ftotal_300).replace('.',','))
                frm_principal.edt_litoral_300.setText(str('%.2f'%ftotall_300).replace('.',','))
            else:
                frm_principal.show
            # Valor do ICMS
            icmsres = (float(valornf)/taxa_icms)-float(valornf) #0.88
            frm_principal.edt_icms.setText(str('%.2f'%icmsres).replace('.',',')) 
        else:
            QMessageBox.about(frm_principal, "Aviso", "Insira o Valor da Nota Fiscal!")
            frm_principal.show()
    else:
        QMessageBox.about(frm_principal, "Aviso", "Insira os valores!")
        frm_principal.show()
def salva_cotacao():
    orig_cnpj = frm_principal.edt_rem_cnpj.text()
    orig_desc = frm_principal.edt_rem_desc.text()
    dest_cnpj = frm_principal.edt_dest_cnpj.text()
    dest_desc = frm_principal.edt_dest_desc.text()
    cidade_origem = frm_principal.edt_rem_cid.text()
    estado_origem = frm_principal.edt_rem_uf.text() 
    cidade_destino = frm_principal.edt_dest_cid.text()
    estado_destino = frm_principal.edt_dest_uf.text() 
    valor_merc = frm_principal.edt_valor_merc.text().replace(',','.')
    peso = frm_principal.edt_peso.text().replace(',','.')
    volume = frm_principal.edt_volume.text() 
    tipo_merc = frm_principal.edit_tipo_merc.text() 
    peso_cudo_total = frm_principal.edit_peso_cubo.text().replace(',','.')
    m3_total = frm_principal.edt_total_m3_2.text().replace(',','.')
    tipo = ""
    if frm_principal.rbtn_cif.isChecked() :
        tipo = "CIF"
    elif frm_principal.rbtn_fob.isChecked() :        
        tipo = "FOB"
    if peso_cudo_total == '':
        peso_cudo_total = 0.00
    if m3_total == '':
        m3_total = 0.00
    """else:
        QMessageBox.about(frm_principal, "Aviso", "Selecione o Tipo do Frete.")"""
    if not tipo == "":
        cursor = banco.cursor()
        comando_sql=("INSERT INTO cotacao(emit_cnpj, emit_nome, dest_cnpj, dest_nome, cidade_origem, estado_origem, cidade_destino, estado_destino, tipo, valor_merc, peso, volume, tipo_merc, peso_cubo_total, m3_total) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        dados=(str(orig_cnpj),str(orig_desc), str(dest_cnpj), str(dest_desc), str(cidade_origem), str(estado_origem), str(cidade_destino), str(estado_destino), str(tipo), float(valor_merc), float(peso), int(volume), str(tipo_merc), float(peso_cudo_total), float(m3_total))
        cursor.execute(comando_sql,dados)
        banco.commit()
        QMessageBox.information(frm_principal, "Aviso", "Cotação salva!")
        # Limpando a tela
        orig_cnpj = frm_principal.edt_rem_cnpj.setText('')
        orig_desc = frm_principal.edt_rem_desc.setText('')
        dest_cnpj = frm_principal.edt_dest_cnpj.setText('')
        dest_desc = frm_principal.edt_dest_desc.setText('')
        cidade_origem = frm_principal.edt_rem_cid.setText('')
        estado_origem = frm_principal.edt_rem_uf.setText('') 
        cidade_destino = frm_principal.edt_dest_cid.setText('')
        estado_destino = frm_principal.edt_dest_uf.setText('')
        valor_merc = frm_principal.edt_valor_merc.setText('')
        peso = frm_principal.edt_peso.setText('')
        volume = frm_principal.edt_volume.setText('')
        tipo_merc = frm_principal.edit_tipo_merc.setText('')
        peso_cudo_total = frm_principal.edit_peso_cubo.setText('')
        m3_total = frm_principal.edt_total_m3_2.setText('')
        tipo = ""
    else:
        QMessageBox.about(frm_principal, "Aviso", "Selecione o Tipo do Frete.")  
def limpar_tela():
    pass
def excluir_m3():
    cursor3 = banco.cursor()
    cursor3.execute("SELECT id FROM cubagem")
    dados_lido = cursor3.fetchall()
    banco.commit()
    result_m3 = 0
    if not dados_lido == []:
        linha = frm_principal.tableWidget.currentRow()
        frm_principal.tableWidget.removeRow(linha)

        cursor = banco.cursor()
        cursor.execute("SELECT * FROM cubagem")
        dados_lidos = cursor.fetchall()
        valor_id = dados_lidos[linha][0]
        cursor.execute("DELETE FROM cubagem WHERE id="+ str(valor_id))
        banco.commit()
        # Subtrai o valor total e Exclui no bando de dado
        cursor2 = banco.cursor()
        cursor2.execute("SELECT * FROM cubagem")
        dados = cursor2.fetchall()
        banco.commit()
        totalm3lista = 0 
        for dado in range(len(dados)):
            lista = float(dados[dado][5])
            totalm3lista = float(totalm3lista + lista)
            result_m3 = totalm3lista / 300
        # Mostra no tela    
        frm_principal.edt_totalPeso_m3.setText(str('%.2f'%totalm3lista).replace('.',','))
        frm_principal.edit_peso_cubo.setText(str('%.2f'%totalm3lista).replace('.',','))
        frm_principal.edt_total_m3.setText(str('%.5f'%result_m3).replace('.',','))
    else:        
        frm_principal.edt_totalPeso_m3.setText('')
        frm_principal.edit_peso_cubo.setText('')
        frm_principal.edt_total_m3.setText('')
def add_m3():
    global id_m3
    global result_peso_m3
    dim1 = float(frm_principal.edt_dim1.text().replace(',','.'))
    dim2 = float(frm_principal.edt_dim2.text().replace(',','.'))
    dim3 = float(frm_principal.edt_dim3.text().replace(',','.'))
    vol = int(frm_principal.edt_vol.text())
    
    resultado = dim1 * dim2 * dim3* vol * 0.3 * 1000
    result_peso_m3 = result_peso_m3 + resultado
    result_m3 = result_peso_m3 / 300
    frm_principal.edt_resultado_m3.setText(str('%.4f'%resultado).replace('.',','))
    frm_principal.edt_totalPeso_m3.setText(str('%.2f'%result_peso_m3).replace('.',','))
    frm_principal.edit_peso_cubo.setText(str('%.2f'%result_peso_m3).replace('.',','))
    frm_principal.edt_total_m3.setText(str('%.5f'%result_m3).replace('.',','))
    frm_principal.edt_total_m3_2.setText(str('%.5f'%result_m3).replace('.',','))

    cursor = banco.cursor()
    comando_sql=("INSERT INTO cubagem(dim1,dim2,dim3,volume,m3) VALUES(%s,%s,%s,%s,%s)")
    dados=(float(dim1),float(dim2),float(dim3),int(vol),float(resultado))
    cursor.execute(comando_sql,dados)
    banco.commit()
    
    cursor2 = banco.cursor()
    comando_SQL = "SELECT dim1, dim2, dim3,volume,m3  FROM cubagem"
    cursor2.execute(comando_SQL)
    dados_lidos = cursor2.fetchall()

    frm_principal.tableWidget.setRowCount(len(dados_lidos))
    frm_principal.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for j in range(0, 5):
            frm_principal.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados_lidos[i][j]))) 

    frm_principal.edt_dim1.setText('')
    frm_principal.edt_dim2.setText('')
    frm_principal.edt_dim3.setText('')
    frm_principal.edt_vol.setText('')
    frm_principal.edt_resultado_m3.setText('')   
def chama_tarifa():
    # Tabela "tarifas_minimas"
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM tarifas_minimas") 
    tabelas = cursor.fetchall()
    total_id = len(tabelas)
    # Tabela "tarifas"
    cursor2 = banco.cursor()
    cursor2.execute("SELECT * FROM tarifas") 
    taxas = cursor2.fetchall()
    total_taxa = len(taxas)
    if total_id != 0:
        frm_tarifa.edt_base_20.setText(str(tabelas[0][2]).replace('.',','))
        frm_tarifa.edt_base_lit_20.setText(str(tabelas[0][3]).replace('.',','))
        frm_tarifa.edt_ad_gris_20.setText(str(tabelas[0][4]).replace('.',','))
        frm_tarifa.edt_pedagio_20.setText(str(tabelas[0][5]).replace('.',','))
        frm_tarifa.edt_pedlitoral_20.setText(str(tabelas[0][6]).replace('.',','))
        frm_tarifa.edt_base_50.setText(str(tabelas[1][2]).replace('.',','))
        frm_tarifa.edt_base_lit_50.setText(str(tabelas[1][3]).replace('.',','))
        frm_tarifa.edt_ad_gris_50.setText(str(tabelas[1][4]).replace('.',','))
        frm_tarifa.edt_pedagio_50.setText(str(tabelas[1][5]).replace('.',','))
        frm_tarifa.edt_pedlitoral_50.setText(str(tabelas[1][6]).replace('.',','))
        frm_tarifa.edt_base_100.setText(str(tabelas[2][2]).replace('.',','))
        frm_tarifa.edt_base_lit_100.setText(str(tabelas[2][3]).replace('.',','))
        frm_tarifa.edt_ad_gris_100.setText(str(tabelas[2][4]).replace('.',','))
        frm_tarifa.edt_pedagio_100.setText(str(tabelas[2][5]).replace('.',','))
        frm_tarifa.edt_pedlitoral_100.setText(str(tabelas[2][6]).replace('.',','))
        frm_tarifa.edt_base_150.setText(str(tabelas[3][2]).replace('.',','))
        frm_tarifa.edt_base_lit_150.setText(str(tabelas[3][3]).replace('.',','))
        frm_tarifa.edt_ad_gris_150.setText(str(tabelas[3][4]).replace('.',','))
        frm_tarifa.edt_pedagio_150.setText(str(tabelas[3][5]).replace('.',','))
        frm_tarifa.edt_pedlitoral_150.setText(str(tabelas[3][6]).replace('.',','))
        frm_tarifa.edt_base_200.setText(str(tabelas[4][2]).replace('.',','))
        frm_tarifa.edt_base_lit_200.setText(str(tabelas[4][3]).replace('.',','))
        frm_tarifa.edt_ad_gris_200.setText(str(tabelas[4][4]).replace('.',','))
        frm_tarifa.edt_pedagio_200.setText(str(tabelas[4][5]).replace('.',','))
        frm_tarifa.edt_pedlitoral_200.setText(str(tabelas[4][6]).replace('.',','))
        frm_tarifa.edt_base_250.setText(str(tabelas[5][2]).replace('.',','))
        frm_tarifa.edt_base_lit_250.setText(str(tabelas[5][3]).replace('.',','))
        frm_tarifa.edt_ad_gris_250.setText(str(tabelas[5][4]).replace('.',','))
        frm_tarifa.edt_pedagio_250.setText(str(tabelas[5][5]).replace('.',','))
        frm_tarifa.edt_pedlitoral_250.setText(str(tabelas[5][6]).replace('.',','))
        frm_tarifa.edt_base_300.setText(str(tabelas[6][2]).replace('.',','))
        frm_tarifa.edt_base_lit_300.setText(str(tabelas[6][3]).replace('.',','))
        frm_tarifa.edt_ad_gris_300.setText(str(tabelas[6][4]).replace('.',','))
        frm_tarifa.edt_pedagio_300.setText(str(tabelas[6][5]).replace('.',','))
        frm_tarifa.edt_pedlitoral_300.setText(str(tabelas[6][6]).replace('.',','))
    if total_taxa != 0:
        frm_tarifa.edt_fpeso.setText(str(taxas[0][2]).replace('.',','))
        frm_tarifa.edt_ad.setText(str(taxas[0][3]).replace('.',','))
        frm_tarifa.edt_gris.setText(str(taxas[0][4]).replace('.',','))
        frm_tarifa.edt_taxa.setText(str(taxas[0][5]).replace('.',','))
        frm_tarifa.edt_icms.setText(str(taxas[0][6]).replace('.',','))
        frm_tarifa.edt_fpeso_lit.setText(str(taxas[1][2]).replace('.',','))
        frm_tarifa.edt_ad_lit.setText(str(taxas[1][3]).replace('.',','))
        frm_tarifa.edt_gris_lit.setText(str(taxas[1][4]).replace('.',','))
        frm_tarifa.edt_taxa_lit.setText(str(taxas[1][5]).replace('.',','))
        frm_tarifa.edt_icms_lit.setText(str(taxas[1][6]).replace('.',','))
    frm_tarifa.show()
def salva_tarifa():
    global numero_id
    desc20 = frm_tarifa.desc_20.text().replace(',','.')
    tBase20 = frm_tarifa.edt_base_20.text().replace(',','.')
    tLit20 = frm_tarifa.edt_base_lit_20.text().replace(',','.')
    ad_gris20 = frm_tarifa.edt_ad_gris_20.text().replace(',','.')
    ped20 = frm_tarifa.edt_pedagio_20.text().replace(',','.')
    pedl20 = frm_tarifa.edt_pedlitoral_20.text().replace(',','.')
    
    desc50 = frm_tarifa.desc_50.text().replace(',','.')
    tBase50 = frm_tarifa.edt_base_50.text().replace(',','.')
    tLit50 = frm_tarifa.edt_base_lit_50.text().replace(',','.')
    ad_gris50 = frm_tarifa.edt_ad_gris_50.text().replace(',','.')
    ped50 = frm_tarifa.edt_pedagio_50.text().replace(',','.')
    pedl50 = frm_tarifa.edt_pedlitoral_50.text().replace(',','.')
    
    desc100 = frm_tarifa.desc_100.text().replace(',','.')
    tBase100 = frm_tarifa.edt_base_100.text().replace(',','.')
    tLit100 = frm_tarifa.edt_base_lit_100.text().replace(',','.')
    ad_gris100 = frm_tarifa.edt_ad_gris_100.text().replace(',','.')
    ped100 = frm_tarifa.edt_pedagio_100.text().replace(',','.')
    pedl100 = frm_tarifa.edt_pedlitoral_100.text().replace(',','.')

    desc150 = frm_tarifa.desc_150.text().replace(',','.')
    tBase150 = frm_tarifa.edt_base_150.text().replace(',','.')
    tLit150 = frm_tarifa.edt_base_lit_150.text().replace(',','.')
    ad_gris150 = frm_tarifa.edt_ad_gris_150.text().replace(',','.')
    ped150 = frm_tarifa.edt_pedagio_150.text().replace(',','.')
    pedl150 = frm_tarifa.edt_pedlitoral_150.text().replace(',','.')

    desc200 = frm_tarifa.desc_200.text().replace(',','.')
    tBase200 = frm_tarifa.edt_base_200.text().replace(',','.')
    tLit200 = frm_tarifa.edt_base_lit_200.text().replace(',','.')
    ad_gris200 = frm_tarifa.edt_ad_gris_200.text().replace(',','.')
    ped200 = frm_tarifa.edt_pedagio_200.text().replace(',','.')
    pedl200 = frm_tarifa.edt_pedlitoral_200.text().replace(',','.')
    
    desc250 = frm_tarifa.desc_250.text().replace(',','.')
    tBase250 = frm_tarifa.edt_base_250.text().replace(',','.')
    tLit250 = frm_tarifa.edt_base_lit_250.text().replace(',','.')
    ad_gris250 = frm_tarifa.edt_ad_gris_250.text().replace(',','.')
    ped250 = frm_tarifa.edt_pedagio_250.text().replace(',','.')
    pedl250 = frm_tarifa.edt_pedlitoral_250.text().replace(',','.')
    
    desc300 = frm_tarifa.desc_300.text().replace(',','.')
    tBase300 = frm_tarifa.edt_base_300.text().replace(',','.')
    tLit300 = frm_tarifa.edt_base_lit_300.text().replace(',','.')
    ad_gris300 = frm_tarifa.edt_ad_gris_300.text().replace(',','.')
    ped300 = frm_tarifa.edt_pedagio_300.text().replace(',','.')
    pedl300 = frm_tarifa.edt_pedlitoral_300.text().replace(',','.')

    cursor = banco.cursor()
    cursor.execute("SELECT id FROM tarifas_minimas")
    dadosid = cursor.fetchall()
    cursor2 = banco.cursor()
    cursor2.execute("SELECT * FROM tarifas_minimas") 
    dados = cursor2.fetchall()
    
    if desc20 == dados[0][1]:
        numero_id = dadosid[0][0]
        cursor = banco.cursor()
        cursor.execute("UPDATE tarifas_minimas SET tarifa_base='{}',tarifa_litoral='{}',ad_Gris='{}',pedagio='{}',pedlitoral='{}' WHERE id={}".format(tBase20,tLit20,ad_gris20,ped20,pedl20,numero_id))
        banco.commit()
    if desc50 == dados[1][1]:
        numero_id = dadosid[1][0]
        cursor = banco.cursor()
        cursor.execute("UPDATE tarifas_minimas SET tarifa_base='{}',tarifa_litoral='{}',ad_Gris='{}',pedagio='{}',pedlitoral='{}' WHERE id={}".format(tBase50,tLit50,ad_gris50,ped50,pedl50,numero_id))
        banco.commit()
    if desc100 == dados[2][1]:
        numero_id = dadosid[2][0]
        cursor = banco.cursor()
        cursor.execute("UPDATE tarifas_minimas SET tarifa_base='{}',tarifa_litoral='{}',ad_Gris='{}',pedagio='{}',pedlitoral='{}' WHERE id={}".format(tBase100,tLit100,ad_gris100,ped100,pedl100,numero_id))
        banco.commit()
    if desc150 == dados[3][1]:
        numero_id = dadosid[3][0]
        cursor = banco.cursor()
        cursor.execute("UPDATE tarifas_minimas SET tarifa_base='{}',tarifa_litoral='{}',ad_Gris='{}',pedagio='{}',pedlitoral='{}' WHERE id={}".format(tBase150,tLit150,ad_gris150,ped150,pedl150,numero_id))
        banco.commit()
    if desc200 == dados[4][1]:
        numero_id = dadosid[4][0]
        cursor = banco.cursor()
        cursor.execute("UPDATE tarifas_minimas SET tarifa_base='{}',tarifa_litoral='{}',ad_Gris='{}',pedagio='{}',pedlitoral='{}' WHERE id={}".format(tBase200,tLit200,ad_gris200,ped200,pedl200,numero_id))
        banco.commit()
    if desc250 == dados[5][1]:
        numero_id = dadosid[5][0]
        cursor = banco.cursor()
        cursor.execute("UPDATE tarifas_minimas SET tarifa_base='{}',tarifa_litoral='{}',ad_Gris='{}',pedagio='{}',pedlitoral='{}' WHERE id={}".format(tBase250,tLit250,ad_gris250,ped250,pedl250,numero_id))
        banco.commit()
    if desc300 == dados[6][1]:
        numero_id = dadosid[6][0]
        cursor = banco.cursor()
        cursor.execute("UPDATE tarifas_minimas SET tarifa_base='{}',tarifa_litoral='{}',ad_Gris='{}',pedagio='{}',pedlitoral='{}' WHERE id={}".format(tBase300,tLit300,ad_gris300,ped300,pedl300,numero_id))
        banco.commit()
    QMessageBox.information(frm_tarifa, "Aviso", "tabela Atualizadas")
def salva_taxa():
    #taxas base
    fPeso = frm_tarifa.edt_fpeso.text().replace(',','.')
    ad_v = frm_tarifa.edt_ad.text().replace(',','.')
    gris = frm_tarifa.edt_gris.text().replace(',','.')
    taxa = frm_tarifa.edt_taxa.text().replace(',','.')
    icms = frm_tarifa.edt_icms.text().replace(',','.')
    # taxas base litoral
    fPesolit = frm_tarifa.edt_fpeso_lit.text().replace(',','.')
    ad_vlit = frm_tarifa.edt_ad_lit.text().replace(',','.')
    grislit = frm_tarifa.edt_gris_lit.text().replace(',','.')
    taxalit = frm_tarifa.edt_taxa_lit.text().replace(',','.')
    icmslit = frm_tarifa.edt_icms_lit.text().replace(',','.')
    cursor2 = banco.cursor()
    cursor2.execute("SELECT * FROM tarifas")
    tarifas = cursor2.fetchall()
    valor_id2 = len(tarifas)
    ids= tarifas
    idtb='TB'
    idtbl="TBL"
    if valor_id2 == 0:
        if ids != idtb:
            cursor = banco.cursor()
            comando_sql=("INSERT INTO tarifas(descricao,frete_peso,ad_valoren,gris,taxa,icms) VALUES(%s,%s,%s,%s,%s,%s)")
            dados=(str('TB'),float(fPeso),float(ad_v),float(gris),float(taxa),float(icms))
            cursor.execute(comando_sql,dados)
            banco.commit()
        if ids != idtbl:
            cursor = banco.cursor()
            comando_sql=("INSERT INTO tarifas(descricao,frete_peso,ad_valoren,gris,taxa,icms) VALUES(%s,%s,%s,%s,%s,%s)")
            dados=(str('TBL'),float(fPesolit),float(ad_vlit),float(grislit),float(taxalit),float(icmslit))
            cursor.execute(comando_sql,dados)
            banco.commit()
        QMessageBox.information(frm_tarifa, "Aviso", "Taxas cadastradas")
        frm_tarifa.show()
    elif valor_id2 != 0:
        if ids[0][1] == idtb:
            cursor = banco.cursor()
            cursor.execute("UPDATE tarifas SET frete_peso='{}',ad_valoren='{}',gris='{}',taxa='{}',icms='{}' WHERE descricao='{}'".format(fPeso,ad_v,gris,taxa,icms,str('TB')))
            banco.commit()
        if ids[1][1] == idtbl:
            cursor = banco.cursor()
            cursor.execute("UPDATE tarifas SET frete_peso='{}',ad_valoren='{}',gris='{}',taxa='{}',icms='{}' WHERE descricao='{}'".format(fPesolit,ad_vlit,grislit,taxalit,icmslit,str('TBL')))
            banco.commit()
            QMessageBox.information(frm_tarifa, "Aviso", "Taxas Atualizadas")
        else:
            QMessageBox.about(frm_tarifa, "ERRO", "Erro na Atualização")
    else:
        QMessageBox.about(frm_tarifa, "ERRO", "falta dados!")
def pesquisa_remente():
    global cliente_id
    global client
    rem_cnpj = frm_principal.edt_rem_cnpj.text()
    rem_desc = frm_principal.edt_rem_desc.text()
    rem_cid = frm_principal.edt_rem_cid.text()
    rem_uf = frm_principal.edt_rem_uf.text()
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cliente")
    cliente = cursor.fetchall()
    dados_lidos = len(cliente)

    if dados_lidos == 0:
        frm_cliente.show()
        frm_cliente.edt_cnpj.setText(str(rem_cnpj))
        frm_cliente.edt_desc.setText(str(rem_desc))
        frm_cliente.edt_cid.setText(str(rem_cid))
    else:
        if not rem_cnpj == '':
            cursor = banco.cursor()
            cursor.execute("SELECT * FROM cliente WHERE cnpj="+ str(rem_cnpj))
            dados_lidos = cursor.fetchall()            
            totalcliente = len(dados_lidos)

            if totalcliente == 0:
                frm_cliente.show()
                frm_cliente.edt_cnpj.setText(str(rem_cnpj))
            else:
                frm_principal.edt_rem_cnpj.setText(str(dados_lidos[0][1]))
                frm_principal.edt_rem_desc.setText(str(dados_lidos[0][2]))
                frm_principal.edt_rem_cid.setText(str(dados_lidos[0][3]))
                frm_principal.edt_rem_uf.setText(str(dados_lidos[0][4]))
        else:
            frm_cliente.show()
            frm_cliente.edt_cnpj.setText(str(rem_cnpj))
    
    cursor1 = banco.cursor()
    cursor1.execute("SELECT cnpj, descricao, cidade, uf FROM  cliente")
    dados_clientes = cursor1.fetchall()
    frm_cliente.tableWidget.setRowCount(len(dados_clientes))
    frm_cliente.tableWidget.setColumnCount(4)
    for i in range(0, len(dados_clientes)):
        for j in range(0, 4):
            frm_cliente.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_clientes[i][j])))
    client = 1
def pesquisa_destinatario():
    global cliente_id
    global client
    dest_cnpj = frm_principal.edt_dest_cnpj.text()
    dest_desc = frm_principal.edt_dest_desc.text()
    dest_cid = frm_principal.edt_dest_cid.text()
    dest_uf = frm_principal.edt_dest_uf.text()
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cliente")
    cliente = cursor.fetchall()
    dados_lidos = len(cliente)
    
    if dados_lidos == 0:
        frm_cliente.show()
        frm_cliente.edt_cnpj.setText(str(dest_cnpj))
        frm_cliente.edt_desc.setText(str(dest_desc))
        frm_cliente.edt_cid.setText(str(dest_cid))
        frm_cliente.edt_uf.text(str(dest_uf))
    else:
        if not dest_cnpj == '':
            cursor = banco.cursor()
            cursor.execute("SELECT * FROM cliente WHERE cnpj="+ str(dest_cnpj))
            dados_lidos = cursor.fetchall()            
            totalcliente = len(dados_lidos)

            if totalcliente == 0:
                frm_cliente.show()
                frm_cliente.edt_cnpj.setText(str(dest_cnpj))
            else:
                frm_principal.edt_dest_cnpj.setText(str(dados_lidos[0][1]))
                frm_principal.edt_dest_desc.setText(str(dados_lidos[0][2]))
                frm_principal.edt_dest_cid.setText(str(dados_lidos[0][3]))
                frm_principal.edt_dest_uf.setText(str(dados_lidos[0][4]))
        else:
            frm_cliente.show()
            frm_cliente.edt_cnpj.setText(str(dest_cnpj))
            
    cursor1 = banco.cursor()
    cursor1.execute("SELECT cnpj, descricao, cidade, uf FROM  cliente")
    dados_clientes = cursor1.fetchall()
    frm_cliente.tableWidget.setRowCount(len(dados_clientes))
    frm_cliente.tableWidget.setColumnCount(4)
    
    for i in range(0, len(dados_clientes)):
        for j in range(0, 4):
            frm_cliente.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_clientes[i][j])))
    client = 2
def cadastro_cliente():
    global cliente
    cnpj = frm_cliente.edt_cnpj.text()
    desc = frm_cliente.edt_desc.text()
    cid = frm_cliente.edt_cid.text()
    uf = frm_cliente.edt_uf.text()
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cliente")
    cliente = cursor.fetchall()
    dados_lidos = len(cliente)

    if dados_lidos == 0:
        frm_cliente.show()
        cursor = banco.cursor()
        comando_sql=("INSERT INTO cliente(cnpj, descricao, cidade, uf) VALUES(%s,%s,%s,%s)")
        dados=(str(cnpj),str(desc),str(cid),str(uf))
        cursor.execute(comando_sql,dados)
        banco.commit()
        QMessageBox.information(frm_tarifa, "Aviso", "Cliente Cadastrado!")
        frm_cliente.close()
    elif dados_lidos != 0:
        cliente_id = cliente[0]
        if cliente_id == cnpj:
            cursor = banco.cursor()
            cursor.execute("UPDATE cliente SET cnpj='{}',descricao='{}',cidade='{}',uf='{}' WHERE id='{}'".format(cnpj,desc,cid,uf, cliente_id))
            banco.commit()
            QMessageBox.information(frm_tarifa, "Aviso", "Cliente Atualizado")
            frm_cliente.close()
        elif cliente_id != cnpj:
            cursor = banco.cursor()
            comando_sql=("INSERT INTO cliente(cnpj, descricao, cidade, uf) VALUES(%s,%s,%s,%s)")
            dados=(str(cnpj),str(desc),str(cid),str(uf))
            cursor.execute(comando_sql,dados)
            banco.commit()
            QMessageBox.information(frm_tarifa, "Aviso", "Cliente Cadastrado!")
        else:
            QMessageBox.about(frm_tarifa, "ERRO", "Erro no Cadastro")
    else:
        QMessageBox.about(frm_tarifa, "ERRO", "falta dados!")
    cursor1 = banco.cursor()
    cursor1.execute("SELECT * FROM  cliente")
    dados_clientes = cursor1.fetchall()
    frm_cliente.tableWidget.setRowCount(len(dados_clientes))
    frm_cliente.tableWidget.setColumnCount(4)
    for i in range(0, len(dados_clientes)):
        for j in range(0, 4):
            frm_cliente.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_clientes[i][j])))
def limpar_cliente():
    cursor = banco.cursor()
    cursor.execute("SELECT id FROM cubagem")
    dados_lido = cursor.fetchall()
    banco.commit()
    if not dados_lido == []:
        linha = frm_principal.tableWidget.currentRow()
        frm_principal.tableWidget.removeRow(linha)

        cursor = banco.cursor()
        cursor.execute("SELECT * FROM cubagem")
        dados_lidos = cursor.fetchall()
        valor_id = dados_lidos[linha][0]
        cursor.execute("DELETE FROM cubagem WHERE id="+ str(valor_id))
        banco.commit()

        cursor1 = banco.cursor()
        cursor1.execute("SELECT cnpj, descricao, cidade, uf FROM  cliente")
        dados_clientes = cursor1.fetchall()
        frm_cliente.tableWidget.setRowCount(len(dados_clientes))
        frm_cliente.tableWidget.setColumnCount(4)
        for i in range(0, len(dados_clientes)):
            for j in range(0, 4):
                frm_cliente.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_clientes[i][j])))
    else:
        QMessageBox.about(frm_tarifa, "ERRO", "Erro ao excluir, selecione o cliente!")
def select_cliente():
    global numero_id
    global client
    linha = frm_cliente.tableWidget.currentRow()
    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM cliente"
    cursor.execute(comando_SQL)
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM cliente WHERE id="+str(valor_id))
    cliente = cursor.fetchall()
    frm_principal.show()
    if client == 1:
        frm_principal.edt_rem_cnpj.setText(str(cliente[0][1]))
        frm_principal.edt_rem_desc.setText(str(cliente[0][2]))
        frm_principal.edt_rem_cid.setText(str(cliente[0][3]))
        frm_principal.edt_rem_uf.setText(str(cliente[0][4]))
    elif client == 2:
        frm_principal.edt_dest_cnpj.setText(str(cliente[0][1]))
        frm_principal.edt_dest_desc.setText(str(cliente[0][2]))
        frm_principal.edt_dest_cid.setText(str(cliente[0][3]))
        frm_principal.edt_dest_uf.setText(str(cliente[0][4]))
    else:
        QMessageBox.about(frm_principal, "Aviso", "Erro no Bando de Dados!")  
    
    frm_cliente.close()
    numero_id = valor_id
def gerar_pdf():
    linha = frm_cotacao.tableWidget.currentRow()
    cursor = banco.cursor()
    cursor.execute("SELECt id FROM cotacao")
    dados_lidos = cursor.fetchall()
    valor_id = dados_lidos[linha][0]
    cursor.execute("SELECT * FROM cotacao WHERE id="+ str(valor_id))
    cotacao = cursor.fetchall()
    print(cotacao)
    x = 0
    y = 0
    pdf = canvas.Canvas("Cotação de frete {}.dpf".format(str(datetime.date.today())))
    pdf.setFont("Times-Bold", 25)
    pdf.drawString(200,800, "Cotação: " + str(cotacao[0][0]))
    pdf.setFont("Times-Bold", 18)
    for i in range(0, len(cotacao)):
        y = y + 25
        x = x + 25
        pdf.drawString(100 -y, 750, str("Remetente: {}".format(cotacao[i][1])))
        pdf.drawString(350 -y, 750,str(cotacao[i][2]))
        pdf.drawString(100 -x, 750-y, str("Destinatário: " + cotacao[i][3]))
        pdf.drawString(350 -y, 750-y,str(cotacao[i][4]))

    pdf.save()
def chama_cotacao():
    # Tabela "cotacao"
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM cotacao") 
    cotacao = cursor.fetchall()
    frm_cotacao.tableWidget.setRowCount(len(cotacao))
    frm_cotacao.tableWidget.setColumnCount(15)
    for i in range(0, len(cotacao)):
        for j in range(0,15):
            frm_cotacao.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(cotacao[i][j])))
    frm_cotacao.show()
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    frm_principal = uic.loadUi(r'.\forms\frm_principal_full.ui')
    frm_tarifa = uic.loadUi(r'.\forms\frm_tarifa.ui')
    frm_cliente = uic.loadUi(r'.\forms\frm_cadastro_cliente.ui')
    frm_cotacao = uic.loadUi(r'.\forms\frm_cotacao.ui')
    # Botões da tela principal
    frm_principal.btn_calcula.clicked.connect(calc_contacao)
    frm_principal.btn_salvar.clicked.connect(salva_cotacao)
    frm_principal.btn_limpa.clicked.connect(limpar_tela)
    frm_principal.btn_adicionar.clicked.connect(add_m3)
    frm_principal.btn_rem_pesq.clicked.connect(pesquisa_remente)
    frm_principal.btn_dest_pesq.clicked.connect(pesquisa_destinatario)
    frm_principal.btn_tarifa.clicked.connect(chama_tarifa)
    frm_principal.btn_excluir.clicked.connect(excluir_m3)
    frm_principal.btn_cotacao.clicked.connect(chama_cotacao)
    # Botões da tela tarifas
    frm_tarifa.btn_salvar_taxa.clicked.connect(salva_taxa)
    frm_tarifa.btn_salvar_tabela.clicked.connect(salva_tarifa)
    # Botões da tela Cadastro de Cliente
    frm_cliente.btn_salvar.clicked.connect(cadastro_cliente)
    frm_cliente.btn_limpar.clicked.connect(limpar_cliente)
    frm_cliente.btn_selecionar.clicked.connect(select_cliente)
    # Botões da tela cotações
    frm_cotacao.btn_dpf.clicked.connect(gerar_pdf)
    #limpar bd.cubagem
    cursor = banco.cursor()
    cursor.execute("TRUNCATE TABLE cubagem") 
    tabelas = cursor.fetchall()
    # Mostrar dados da tabelas "tarifas_minimas"
    cursor4 = banco.cursor()
    cursor4.execute("SELECT * FROM tarifas_minimas") 
    tabelas = cursor4.fetchall()
    tabela = len(tabelas)
    if not tabela == 0:
        frm_principal.edt_base_20.setText(str(tabelas[0][2]).replace('.',','))
        frm_principal.edt_base_lit_20.setText(str(tabelas[0][3]).replace('.',','))
        frm_principal.edt_ad_gris_20.setText(str(tabelas[0][4]).replace('.',','))
        frm_principal.edt_pedagio_20.setText(str(tabelas[0][5]).replace('.',','))
        frm_principal.edt_pedlitoral_20.setText(str(tabelas[0][6]).replace('.',','))

        frm_principal.edt_base_50.setText(str(tabelas[1][2]).replace('.',','))
        frm_principal.edt_base_lit_50.setText(str(tabelas[1][3]).replace('.',','))
        frm_principal.edt_ad_gris_50.setText(str(tabelas[1][4]).replace('.',','))
        frm_principal.edt_pedagio_50.setText(str(tabelas[1][5]).replace('.',','))
        frm_principal.edt_pedlitoral_50.setText(str(tabelas[1][6]).replace('.',','))

        frm_principal.edt_base_100.setText(str(tabelas[2][2]).replace('.',','))
        frm_principal.edt_base_lit_100.setText(str(tabelas[2][3]).replace('.',','))
        frm_principal.edt_ad_gris_100.setText(str(tabelas[2][4]).replace('.',','))
        frm_principal.edt_pedagio_100.setText(str(tabelas[2][5]).replace('.',','))
        frm_principal.edt_pedlitoral_100.setText(str(tabelas[2][6]).replace('.',','))

        frm_principal.edt_base_150.setText(str(tabelas[3][2]).replace('.',','))
        frm_principal.edt_base_lit_150.setText(str(tabelas[3][3]).replace('.',','))
        frm_principal.edt_ad_gris_150.setText(str(tabelas[3][4]).replace('.',','))
        frm_principal.edt_pedagio_150.setText(str(tabelas[3][5]).replace('.',','))
        frm_principal.edt_pedlitoral_150.setText(str(tabelas[3][6]).replace('.',','))

        frm_principal.edt_base_200.setText(str(tabelas[4][2]).replace('.',','))
        frm_principal.edt_base_lit_200.setText(str(tabelas[4][3]).replace('.',','))
        frm_principal.edt_ad_gris_200.setText(str(tabelas[4][4]).replace('.',','))
        frm_principal.edt_pedagio_200.setText(str(tabelas[4][5]).replace('.',','))
        frm_principal.edt_pedlitoral_200.setText(str(tabelas[4][6]).replace('.',','))

        frm_principal.edt_base_250.setText(str(tabelas[5][2]).replace('.',','))
        frm_principal.edt_base_lit_250.setText(str(tabelas[5][3]).replace('.',','))
        frm_principal.edt_ad_gris_250.setText(str(tabelas[5][4]).replace('.',','))
        frm_principal.edt_pedagio_250.setText(str(tabelas[5][5]).replace('.',','))
        frm_principal.edt_pedlitoral_250.setText(str(tabelas[5][6]).replace('.',','))

        frm_principal.edt_base_300.setText(str(tabelas[6][2]).replace('.',','))
        frm_principal.edt_base_lit_300.setText(str(tabelas[6][3]).replace('.',','))
        frm_principal.edt_ad_gris_300.setText(str(tabelas[6][4]).replace('.',','))
        frm_principal.edt_pedagio_300.setText(str(tabelas[6][5]).replace('.',','))
        frm_principal.edt_pedlitoral_300.setText(str(tabelas[6][6]).replace('.',','))

    # __name__ == "__main__"
    frm_principal.show()
    app.exec()