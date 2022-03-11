from inspect import trace
from pickle import TRUE
from unittest import result
from PyQt5 import uic, QtWidgets
import mysql.connector
import pandas as pd
banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="cofggcvf",
    database="cotacao"
)

dim1 = float(input('digite medida 1: '))
dim2 = 0.23
dim3 = 0.23
vol = 3

resultado = float(dim1 * dim2 * dim3 * vol* 0.3*1000)

len_result = 0
restotal =0

while len_result == 0:
    len_result = len_result + 1
    restotal = restotal+resultado 
    dim1 = float(input('digite medida 1: '))

#print(resultado)
print(type(resultado))
print(str('%.4f'%resultado).replace('.',','))
print(str('%.4f'%restotal).replace('.',','))