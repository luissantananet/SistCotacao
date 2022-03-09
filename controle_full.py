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
global numero_id
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

    valornf=frm_principal.edt_valor_merc.text()
    peso=frm_principal.edt_peso.text()
    if valornf != "" or peso != "":
        if peso != "":
            fpesores = float(peso) * taxa_fpeso #0.52
            frm_principal.edt_fpeso.setText(str('%.2f'%fpesores))
        else:
            QMessageBox.about(frm_principal, "Aviso", "Insira o Peso!")
            frm_principal.show()
        if valornf != "":
            # Valor GRIS
            valorgris = float(valornf) * taxa_gris #0.0025 #/0.88+1.92
            frm_principal.edt_gris.setText(str('%.4f'%valorgris)) 
            # Valor Ad_Valoren
            vaload = float(valornf) * taxa_ad #0.005
            frm_principal.edt_ad.setText(str('%.4f'%vaload))
            # Valor pedagio
            if peso != "":
                valorped = float(tabelas_ped) *float(peso) / 100 #3.04
                frm_principal.edt_pedag.setText(str('%.3f'%valorped))
                # Valor taxa 
                valortaxa = float(valorped) + taxa_taxas #36.68
                frm_principal.edt_taxas.setText(str('%.2f'%valortaxa))
                # Valor frete cif
                valorcif = float(fpesores) + float(valorgris) + float(vaload) + float(valortaxa)
                frm_principal.edt_frete_cif.setText(str('%.2f'%valorcif))
                valorfob = float(valorcif) / taxa_icms #0.88
                frm_principal.edt_frete_fob.setText(str('%.2f'%valorfob))
                # Valor frete litoral
                fpresol = float(peso) * taxa_fpesol
                valorgrisl = float(valornf) * taxa_grisl
                valoadl = float(valornf) * taxa_adl
                valortaxal = float(valorped) + taxa_taxasl
                valorlitoral = float(fpresol) + float(valorgrisl) + float(valoadl) + float(valortaxal) + float(taxa_icmsl)
                frm_principal.edt_frete_litoral.setText(str('%.2f'%valorlitoral))
                # Calculo da tabelas
                adg20 = float(tabelas[0][4])
                fb20 = float(tabelas[0][2])
                fbl20 = float(tabelas[0][3])
                ad_g20 = float(valornf) + adg20
                ped20 = float(tabelas[0][5])
                pedl20 = float( tabelas[0][6])
                ftotal_20 = fb20 + ped20 + ad_g20
                ftotall_20 = float(fbl20 + pedl20 + ad_g20)
                frm_principal.edt_ftotal_20.setText(str(ftotal_20))
                frm_principal.edt_litoral_20.setText(str(ftotall_20))

                adg50 = float(tabelas[1][4])
                fb50 = float(tabelas[1][2])
                fbl50 = float(tabelas[1][3])
                ad_g50 = float(valornf) + adg50
                ped50 = float(tabelas[1][5])
                pedl50 = float( tabelas[1][6])
                ftotal_50 = fb50 + ped50 + ad_g50
                ftotall_50 = float(fbl50 + pedl50 + ad_g50)
                frm_principal.edt_ftotal_50.setText(str(ftotal_50))
                frm_principal.edt_litoral_50.setText(str(ftotall_50))

                adg100 = float(tabelas[2][4])
                fb100 = float(tabelas[2][2])
                fbl100 = float(tabelas[2][3])
                ad_g100 = float(valornf) + adg100
                ped100 = float(tabelas[2][5])
                pedl100 = float( tabelas[2][6])
                ftotal_100 = fb100 + ped100 + ad_g100
                ftotall_100 = float(fbl100 + pedl100 + ad_g100)
                frm_principal.edt_ftotal_100.setText(str(ftotal_100))
                frm_principal.edt_litoral_100.setText(str(ftotall_100))

                adg150 = float(tabelas[3][4])
                fb150 = float(tabelas[3][2])
                fbl150 = float(tabelas[3][3])
                ad_g150 = float(valornf) + adg150
                ped150 = float(tabelas[3][5])
                pedl150 = float( tabelas[3][6])
                ftotal_150 = fb150 + ped150 + ad_g150
                ftotall_150 = float(fbl150 + pedl150 + ad_g150)
                frm_principal.edt_ftotal_150.setText(str(ftotal_150))
                frm_principal.edt_litoral_150.setText(str(ftotall_150))

                adg200 = float(tabelas[4][4])
                fb200 = float(tabelas[4][2])
                fbl200 = float(tabelas[4][3])
                ad_g200 = float(valornf) + adg200
                ped200 = float(tabelas[4][5])
                pedl200 = float( tabelas[4][6])
                ftotal_200 = fb200 + ped200 + ad_g200
                ftotall_200 = float(fbl200 + pedl200 + ad_g200)
                frm_principal.edt_ftotal_200.setText(str(ftotal_200))
                frm_principal.edt_litoral_200.setText(str(ftotall_200))

                adg250 = float(tabelas[5][4])
                fb250 = float(tabelas[5][2])
                fbl250 = float(tabelas[5][3])
                ad_g250 = float(valornf) + adg250
                ped250 = float(tabelas[5][5])
                pedl250 = float( tabelas[5][6])
                ftotal_250 = fb250 + ped250 + ad_g250
                ftotall_250 = float(fbl250 + pedl250 + ad_g250)
                frm_principal.edt_ftotal_250.setText(str(ftotal_250))
                frm_principal.edt_litoral_250.setText(str(ftotall_250))

                adg300 = float(tabelas[6][4])
                fb300 = float(tabelas[6][2])
                fbl300 = float(tabelas[6][3])
                ad_g300 = float(valornf) + adg300
                ped300 = float(tabelas[6][5])
                pedl300 = float( tabelas[6][6])
                ftotal_300 = fb300 + ped300 + ad_g300
                ftotall_300 = float(fbl300 + pedl300 + ad_g300)
                frm_principal.edt_ftotal_300.setText(str(ftotal_300))
                frm_principal.edt_litoral_300.setText(str(ftotall_300))

            else:
                frm_principal.show
            # Valor do ICMS
            icmsres = (float(valornf)/taxa_icms)-float(valornf) #0.88
            frm_principal.edt_icms.setText(str('%.2f'%icmsres)) 
        else:
            QMessageBox.about(frm_principal, "Aviso", "Insira o Valor da Nota Fiscal!")
            frm_principal.show()
    else:
        QMessageBox.about(frm_principal, "Aviso", "Insira os valores!")
        frm_principal.show()
def salva_cotacao():
    pass
def limpar_tela():
    pass
def add_m3():
    pass
def pesquisa_cliente():
    pass
def chama_tarifa():
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM tarifas_minimas") 
    tabelas = cursor.fetchall()
    total_id = len(tabelas)

    cursor2 = banco.cursor()
    cursor2.execute("SELECT * FROM tarifas") 
    taxas = cursor2.fetchall()
    total_taxa = len(taxas)

    if total_id != 0:
        frm_tarifa.edt_base_20.setText(str(tabelas[0][2]))
        frm_tarifa.edt_base_lit_20.setText(str(tabelas[0][3]))
        frm_tarifa.edt_ad_gris_20.setText(str(tabelas[0][4]))
        frm_tarifa.edt_pedagio_20.setText(str(tabelas[0][5]))
        frm_tarifa.edt_pedlitoral_20.setText(str(tabelas[0][6]))
        frm_tarifa.edt_base_50.setText(str(tabelas[1][2]))
        frm_tarifa.edt_base_lit_50.setText(str(tabelas[1][3]))
        frm_tarifa.edt_ad_gris_50.setText(str(tabelas[1][4]))
        frm_tarifa.edt_pedagio_50.setText(str(tabelas[1][5]))
        frm_tarifa.edt_pedlitoral_50.setText(str(tabelas[1][6]))
        frm_tarifa.edt_base_100.setText(str(tabelas[2][2]))
        frm_tarifa.edt_base_lit_100.setText(str(tabelas[2][3]))
        frm_tarifa.edt_ad_gris_100.setText(str(tabelas[2][4]))
        frm_tarifa.edt_pedagio_100.setText(str(tabelas[2][5]))
        frm_tarifa.edt_pedlitoral_100.setText(str(tabelas[2][6]))
        frm_tarifa.edt_base_150.setText(str(tabelas[3][2]))
        frm_tarifa.edt_base_lit_150.setText(str(tabelas[3][3]))
        frm_tarifa.edt_ad_gris_150.setText(str(tabelas[3][4]))
        frm_tarifa.edt_pedagio_150.setText(str(tabelas[3][5]))
        frm_tarifa.edt_pedlitoral_150.setText(str(tabelas[3][6]))
        frm_tarifa.edt_base_200.setText(str(tabelas[4][2]))
        frm_tarifa.edt_base_lit_200.setText(str(tabelas[4][3]))
        frm_tarifa.edt_ad_gris_200.setText(str(tabelas[4][4]))
        frm_tarifa.edt_pedagio_200.setText(str(tabelas[4][5]))
        frm_tarifa.edt_pedlitoral_200.setText(str(tabelas[4][6]))
        frm_tarifa.edt_base_250.setText(str(tabelas[5][2]))
        frm_tarifa.edt_base_lit_250.setText(str(tabelas[5][3]))
        frm_tarifa.edt_ad_gris_250.setText(str(tabelas[5][4]))
        frm_tarifa.edt_pedagio_250.setText(str(tabelas[5][5]))
        frm_tarifa.edt_pedlitoral_250.setText(str(tabelas[5][6]))
        frm_tarifa.edt_base_300.setText(str(tabelas[6][2]))
        frm_tarifa.edt_base_lit_300.setText(str(tabelas[6][3]))
        frm_tarifa.edt_ad_gris_300.setText(str(tabelas[6][4]))
        frm_tarifa.edt_pedagio_300.setText(str(tabelas[6][5]))
        frm_tarifa.edt_pedlitoral_300.setText(str(tabelas[6][6]))
    if total_taxa != 0:
        frm_tarifa.edt_fpeso.setText(str(taxas[0][2]))
        frm_tarifa.edt_ad.setText(str(taxas[0][3]))
        frm_tarifa.edt_gris.setText(str(taxas[0][4]))
        frm_tarifa.edt_taxa.setText(str(taxas[0][5]))
        frm_tarifa.edt_icms.setText(str(taxas[0][6]))
        frm_tarifa.edt_fpeso_lit.setText(str(taxas[1][2]))
        frm_tarifa.edt_ad_lit.setText(str(taxas[1][3]))
        frm_tarifa.edt_gris_lit.setText(str(taxas[1][4]))
        frm_tarifa.edt_taxa_lit.setText(str(taxas[1][5]))
        frm_tarifa.edt_icms_lit.setText(str(taxas[1][6]))

    frm_tarifa.show()

def salva_tarifa():
    global numero_id
    desc20 = frm_tarifa.desc_20.text()
    tBase20 = frm_tarifa.edt_base_20.text()
    tLit20 = frm_tarifa.edt_base_lit_20.text()
    ad_gris20 = frm_tarifa.edt_ad_gris_20.text()
    ped20 = frm_tarifa.edt_pedagio_20.text()
    pedl20 = frm_tarifa.edt_pedlitoral_20.text()
    
    desc50 = frm_tarifa.desc_50.text()
    tBase50 = frm_tarifa.edt_base_50.text()
    tLit50 = frm_tarifa.edt_base_lit_50.text()
    ad_gris50 = frm_tarifa.edt_ad_gris_50.text()
    ped50 = frm_tarifa.edt_pedagio_50.text()
    pedl50 = frm_tarifa.edt_pedlitoral_50.text()
    
    desc100 = frm_tarifa.desc_100.text()
    tBase100 = frm_tarifa.edt_base_100.text()
    tLit100 = frm_tarifa.edt_base_lit_100.text()
    ad_gris100 = frm_tarifa.edt_ad_gris_100.text()
    ped100 = frm_tarifa.edt_pedagio_100.text()
    pedl100 = frm_tarifa.edt_pedlitoral_100.text()

    desc150 = frm_tarifa.desc_150.text()
    tBase150 = frm_tarifa.edt_base_150.text()
    tLit150 = frm_tarifa.edt_base_lit_150.text()
    ad_gris150 = frm_tarifa.edt_ad_gris_150.text()
    ped150 = frm_tarifa.edt_pedagio_150.text()
    pedl150 = frm_tarifa.edt_pedlitoral_150.text()

    desc200 = frm_tarifa.desc_200.text()
    tBase200 = frm_tarifa.edt_base_200.text()
    tLit200 = frm_tarifa.edt_base_lit_200.text()
    ad_gris200 = frm_tarifa.edt_ad_gris_200.text()
    ped200 = frm_tarifa.edt_pedagio_200.text()
    pedl200 = frm_tarifa.edt_pedlitoral_200.text()
    
    desc250 = frm_tarifa.desc_250.text()
    tBase250 = frm_tarifa.edt_base_250.text()
    tLit250 = frm_tarifa.edt_base_lit_250.text()
    ad_gris250 = frm_tarifa.edt_ad_gris_250.text()
    ped250 = frm_tarifa.edt_pedagio_250.text()
    pedl250 = frm_tarifa.edt_pedlitoral_250.text()
    
    desc300 = frm_tarifa.desc_300.text()
    tBase300 = frm_tarifa.edt_base_300.text()
    tLit300 = frm_tarifa.edt_base_lit_300.text()
    ad_gris300 = frm_tarifa.edt_ad_gris_300.text()
    ped300 = frm_tarifa.edt_pedagio_300.text()
    pedl300 = frm_tarifa.edt_pedlitoral_300.text()

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
    desc = frm_tarifa.label_37.text()
    fPeso = frm_tarifa.edt_fpeso.text()
    ad_v = frm_tarifa.edt_ad.text()
    gris = frm_tarifa.edt_gris.text()
    taxa = frm_tarifa.edt_taxa.text()
    icms = frm_tarifa.edt_icms.text()
    # taxas base litoral
    fPesolit = frm_tarifa.edt_fpeso_lit.text()
    ad_vlit = frm_tarifa.edt_ad_lit.text()
    grislit = frm_tarifa.edt_gris_lit.text()
    taxalit = frm_tarifa.edt_taxa_lit.text()
    icmslit = frm_tarifa.edt_icms_lit.text()
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
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    frm_principal = uic.loadUi(r'.\Forms\frm_principal_full.ui')
    frm_tarifa = uic.loadUi(r'.\Forms\frm_tarifa.ui')

    cursor4 = banco.cursor()
    cursor4.execute("SELECT * FROM tarifas_minimas") 
    tabelas = cursor4.fetchall()
    frm_principal.edt_base_20.setText(str(tabelas[0][2]))
    frm_principal.edt_base_lit_20.setText(str(tabelas[0][3]))
    frm_principal.edt_ad_gris_20.setText(str(tabelas[0][4]))
    frm_principal.edt_pedagio_20.setText(str(tabelas[0][5]))
    frm_principal.edt_pedlitoral_20.setText(str(tabelas[0][6]))

    frm_principal.edt_base_50.setText(str(tabelas[1][2]))
    frm_principal.edt_base_lit_50.setText(str(tabelas[1][3]))
    frm_principal.edt_ad_gris_50.setText(str(tabelas[1][4]))
    frm_principal.edt_pedagio_50.setText(str(tabelas[1][5]))
    frm_principal.edt_pedlitoral_50.setText(str(tabelas[1][6]))

    frm_principal.edt_base_100.setText(str(tabelas[2][2]))
    frm_principal.edt_base_lit_100.setText(str(tabelas[2][3]))
    frm_principal.edt_ad_gris_100.setText(str(tabelas[2][4]))
    frm_principal.edt_pedagio_100.setText(str(tabelas[2][5]))
    frm_principal.edt_pedlitoral_100.setText(str(tabelas[2][6]))

    frm_principal.edt_base_150.setText(str(tabelas[3][2]))
    frm_principal.edt_base_lit_150.setText(str(tabelas[3][3]))
    frm_principal.edt_ad_gris_150.setText(str(tabelas[3][4]))
    frm_principal.edt_pedagio_150.setText(str(tabelas[3][5]))
    frm_principal.edt_pedlitoral_150.setText(str(tabelas[3][6]))

    frm_principal.edt_base_200.setText(str(tabelas[4][2]))
    frm_principal.edt_base_lit_200.setText(str(tabelas[4][3]))
    frm_principal.edt_ad_gris_200.setText(str(tabelas[4][4]))
    frm_principal.edt_pedagio_200.setText(str(tabelas[4][5]))
    frm_principal.edt_pedlitoral_200.setText(str(tabelas[4][6]))

    frm_principal.edt_base_250.setText(str(tabelas[5][2]))
    frm_principal.edt_base_lit_250.setText(str(tabelas[5][3]))
    frm_principal.edt_ad_gris_250.setText(str(tabelas[5][4]))
    frm_principal.edt_pedagio_250.setText(str(tabelas[5][5]))
    frm_principal.edt_pedlitoral_250.setText(str(tabelas[5][6]))

    frm_principal.edt_base_300.setText(str(tabelas[6][2]))
    frm_principal.edt_base_lit_300.setText(str(tabelas[6][3]))
    frm_principal.edt_ad_gris_300.setText(str(tabelas[6][4]))
    frm_principal.edt_pedagio_300.setText(str(tabelas[6][5]))
    frm_principal.edt_pedlitoral_300.setText(str(tabelas[6][6]))
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