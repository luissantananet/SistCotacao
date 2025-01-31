from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QTableWidget, QTableWidgetItem
from database import Database 

import mysql.connector
import mysql.connector.errors

import datetime

"""from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4"""
import os

class Cotacao:
    def __init__(self):
        self.db = Database()
        self.db.connect()
        id_txm =len(self.db.selects_all('tarifas_minimas'))
        id_tx = len(self.db.selects_all('tarifas'))
        if id_tx and id_txm == 0:
            self.db.insert_tarifas() 
    def chama_cotacao(self):
        # Tabela "cotacao"
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM cotacao") 
        cotacao = cursor.fetchall()
        frm_cotacao.tableWidget.setRowCount(len(cotacao))
        frm_cotacao.tableWidget.setColumnCount(15)
        for i in range(0, len(cotacao)):
            for j in range(0,15):
                frm_cotacao.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(cotacao[i][j])))
        frm_cotacao.show()
        
    def calc_contacao(self):
        # Acesso as Taxas e tabelas fixas no banco de dados
        taxas = self.db.selects_all('tarifas')
        tabelas = self.db.selects_all('tarifas_minimas')
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
    def chama_tarifa(self):
        tabelas = self.db.selects_all('tarifas_minimas')
        id_tabela_minimas = len(tabelas)
        # tabela tarifas
        taxas = self.db.selects_all('tarifas')
        id_taxas = len(taxas)
        if id_tabela_minimas == 0:
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
        if id_taxas != 0:
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
    def salva_taxa(self):
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
        # Tabela tarifas
        ids = self.db.selects_all('tarifas')
        id_taxas = len(ids)
        if id_taxas == 0:
            self.db.inserts_all('tarifas', {
                'descricao': 'TB',
                'frete_peso': fPeso,
                'ad_valoren': ad_v,
                'gris': gris,
                'taxa': taxa,
                'icms': icms
            })
            self.db.inserts_all('tarifas', {
                'descricao': 'TBL',
                'frete_peso': fPesolit,
                'ad_valoren': ad_vlit,
                'gris': grislit,
                'taxa': taxalit,
                'icms': icmslit
            })
            QMessageBox.information(frm_tarifa, "Aviso", "Taxas salvas com sucesso!")
        else:
            self.db.updeate_all('tarifas', {
                'descricao': 'TB',
                'frete_peso': fPeso,
                'ad_valoren': ad_v,
                'gris': gris,
                'taxa': taxa,
                'icms': icms
            })
            self.db.updeate_all('tarifas', {
                'descricao': 'TBL',
                'frete_peso': fPesolit,
                'ad_valoren': ad_vlit,
                'gris': grislit,
                'taxa': taxalit,
                'icms': icmslit
            })
            QMessageBox.information(frm_tarifa, "Aviso", "Taxas atualizadas com sucesso!")
        frm_tarifa.show()
    def salva_tarifa(self):
        pass
    def limpar_tela(self):
        self.db.delete_all('cubagem')
        frm_principal.edt_rem_cnpj.setText('')
        frm_principal.edt_rem_desc.setText('')
        frm_principal.edt_dest_cnpj.setText('')
        frm_principal.edt_dest_desc.setText('')
        frm_principal.edt_rem_cid.setText('')
        frm_principal.edt_rem_uf.setText('') 
        frm_principal.edt_dest_cid.setText('')
        frm_principal.edt_dest_uf.setText('')
        frm_principal.edt_valor_merc.setText('')
        frm_principal.edt_peso.setText('')
        frm_principal.edt_volume.setText('')
        frm_principal.edit_tipo_merc.setText('')
        frm_principal.edit_peso_cubo.setText('')
        frm_principal.edt_total_m3_2.setText('')
        frm_principal.edt_totalPeso_m3.setText('')
        frm_principal.edit_peso_cubo.setText('')
        frm_principal.edt_total_m3.setText('')
        frm_principal.edt_total_m3_2.setText('')
        frm_principal.edt_resultado_m3.setText('')
        frm_principal.edt_dim1.setText('')
        frm_principal.edt_dim2.setText('')
        frm_principal.edt_dim3.setText('')
        frm_principal.edt_vol.setText('')
        dados = self.db.selects_all('cubagem')
        
        frm_principal.tableWidget.setRowCount(len(dados))
        frm_principal.tableWidget.setColumnCount(5)
        for i in range(0, len(dados)):
            for j in range(0,5):
                frm_principal.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))
    
    def limpar_entrada(self, texto):
        return ''.join(c for c in texto if c.isdigit() or c == '.')

    def add_m3(self):
        dim1 = float(self.limpar_entrada(frm_principal.edt_dim1.text().replace(',','.')))
        dim2 = float(self.limpar_entrada(frm_principal.edt_dim2.text().replace(',','.')))
        dim3 = float(self.limpar_entrada(frm_principal.edt_dim3.text().replace(',','.')))
        vol = int(self.limpar_entrada(frm_principal.edt_vol.text()))
        # Calculo do peso cubico
        result_peso = 0
        result = dim1 * dim2 * dim3 * vol * 0.3 * 1000
        result_peso = result_peso + result
        result_m3 = result_peso / 300
        # Mostrar resultado
        frm_principal.edt_resultado_m3.setText(str('%.4f'%result).replace('.',','))
        frm_principal.edt_totalPeso_m3.setText(str('%.2f'%result_peso).replace('.',','))
        frm_principal.edit_peso_cubo.setText(str('%.2f'%result_peso).replace('.',','))
        frm_principal.edt_total_m3.setText(str('%.5f'%result_m3).replace('.',','))
        frm_principal.edt_total_m3_2.setText(str('%.5f'%result_m3).replace('.',','))
        # Salvar no banco de dados
        self.db.inserts_all('cubagem', {
            'dim1': dim1,
            'dim2': dim2,
            'dim3': dim3,
            'volume': vol,
            'm3': result
        })
        # Mostrar na tabela
        dados = self.db.selects_all('cubagem')
        frm_principal.tableWidget.setRowCount(len(dados))
        frm_principal.tableWidget.setColumnCount(5)
        for i in range(0, len(dados)):
            for j in range(0, 5):
                frm_principal.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j]))) 





if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    frm_principal = uic.loadUi(r'.\forms\frm_principal_full.ui')
    frm_tarifa = uic.loadUi(r'.\forms\frm_tarifa.ui')
    frm_cliente = uic.loadUi(r'.\forms\frm_cadastro_cliente.ui')
    frm_cotacao = uic.loadUi(r'.\forms\frm_cotacao.ui')
    cotacao = Cotacao()
    # Botões da tela principal
    frm_principal.btn_calcula.clicked.connect(cotacao.calc_contacao)
    frm_principal.btn_tarifa.clicked.connect(cotacao.chama_tarifa)

    # Botões da tela tarifas
    frm_tarifa.btn_salvar_taxa.clicked.connect(cotacao.salva_taxa)
    frm_tarifa.btn_salvar_tabela.clicked.connect(cotacao.salva_tarifa)
    frm_principal.btn_limpa.clicked.connect(cotacao.limpar_tela)
    frm_principal.btn_adicionar.clicked.connect(cotacao.add_m3)
    """ frm_principal.btn_salvar.clicked.connect(salva_cotacao)
    
    
    frm_principal.btn_rem_pesq.clicked.connect(pesquisa_remente)
    frm_principal.btn_dest_pesq.clicked.connect(pesquisa_destinatario)
    
    frm_principal.btn_excluir.clicked.connect(excluir_m3)
    frm_principal.btn_cotacao.clicked.connect(cotacao.chama_cotacao)
    
    # Botões da tela Cadastro de Cliente
    frm_cliente.btn_salvar.clicked.connect(cadastro_cliente)
    frm_cliente.btn_limpar.clicked.connect(limpar_cliente)
    frm_cliente.btn_selecionar.clicked.connect(select_cliente)
    # Botões da tela cotações
    frm_cotacao.btn_dpf.clicked.connect(gerar_pdf)"""
    #limpar bd.cubagem
    db = Database()
    db.connect()
    db.create_tables()

    limpar_cubagem = db.TRUNCATE_TABLE('cubagem')
    # Mostrar dados da tabelas "tarifas_minimas"
    tabelas = db.selects_all('tarifas_minimas')
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
    frm_principal.show()
    app.exec()