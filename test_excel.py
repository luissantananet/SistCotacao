import xlrd
from openpyxl import Workbook, load_workbook


planilha = load_workbook("cidades.xls")
aba_ativa = planilha.active
xlin =p.col_values(0)
ylin =p.col_values(0)
