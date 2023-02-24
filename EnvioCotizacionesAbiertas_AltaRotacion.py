import os
import datetime as dt
import pandas as pd
import pyodbc
import numpy as np
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import ascii_uppercase
from openpyxl.styles import Font, NamedStyle,PatternFill
from openpyxl.styles.borders import Border, Side
import openpyxl
import smtplib

#Credenciales del servidor en SQL SERVER
direccion_servidor = '192.168.2.215'
nombre_bd = 'MSTR_DWRXEL'
nombre_usuario = 'useretl'
password = '$R37rmr*@GBdzih@'

#1 GENERAMOS LA CONEXION
try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)
    print('Conexion Exitosa al 215')
except Exception as e:
    # Atrapar error
    print("Ocurrió un error al conectar a SQL Server: ", e)


today=str(dt.datetime.now())