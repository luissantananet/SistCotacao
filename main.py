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
    def chama_cotacao(self):
        # Tabela "cotacao"
        db = Database.connect()
        cursor = db.cursor()
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
    cotacao = Cotacao()
    """ # Botões da tela principal
    frm_principal.btn_calcula.clicked.connect(calc_contacao)
    frm_principal.btn_salvar.clicked.connect(salva_cotacao)
    frm_principal.btn_limpa.clicked.connect(limpar_tela)
    frm_principal.btn_adicionar.clicked.connect(add_m3)
    frm_principal.btn_rem_pesq.clicked.connect(pesquisa_remente)
    frm_principal.btn_dest_pesq.clicked.connect(pesquisa_destinatario)
    frm_principal.btn_tarifa.clicked.connect(chama_tarifa)
    frm_principal.btn_excluir.clicked.connect(excluir_m3)
    frm_principal.btn_cotacao.clicked.connect(cotacao.chama_cotacao)
    # Botões da tela tarifas
    frm_tarifa.btn_salvar_taxa.clicked.connect(salva_taxa)
    frm_tarifa.btn_salvar_tabela.clicked.connect(salva_tarifa)
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