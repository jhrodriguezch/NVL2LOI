#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 17:27:35 2019

@author: girehe2o
"""
import os
import pandas as pd
import numpy as np
#|import matplotlib.pyplot as plt

# ------------ CAMBIAR NOMBRE DE ARCHIVO --------------------------------------
arch_name = 'ts_c_341500.csv'
# ------------ CAMBIAR NOMBRE DE ENTRADA --------------------------------------
Nombre_Archivo = 'CIENAGA_341500'
# -----------------------------------------------------------------------------

os.chdir('C:/Users/57314/Desktop/MEGIA/NVL2LOI/NVL2LOI')

# Cargas el csv seleccion del año de trabajo (25%)

os.chdir('./Datos/corregidos')
df_trb = pd.read_csv(arch_name)

ano_ejecucion = 2013

# Conversion .loi (75%)
dia = []
mes = []
ano = []
for i in np.arange(len(df_trb)):
    fecha = df_trb['Fecha'][i]
    ano.append((fecha[0:4]))
    mes.append(int(fecha[5:7]))
    dia.append(int(fecha[-2:]))
    
fechas = pd.DataFrame({'year' : ano,
                       'month' : mes,
                       'day' : dia})
df_datos = pd.to_datetime(fechas)

df_real = pd.DataFrame()
df_real ['valor'] = df_trb['VALOR']
df_real ['fecha'] = df_datos

# Seleccion de año de trabajo
df_trabajo = df_real [df_real['fecha'].dt.year == ano_ejecucion].copy()

# Configuración datos de salida 
temp_day = np.arange(1, len(df_trabajo) + 1)
val_sec = pd.DataFrame()
val_sec ['tiempo'] = 86400 * temp_day
val_trb = pd.DataFrame()
val_trb ['valor'] = df_trabajo['valor'].copy()


# Creación de .loi

# Archivo para calentamiento
os.chdir('C:/Users/57314/Desktop/MEGIA/NVL2LOI/NVL2LOI/Resultados')
arch = open('Q_' + arch_name[3:-4].upper() + '_cal.loi', 'w')

arch.write('# ' + Nombre_Archivo + '\n')
arch.write('# Temps (s) Debit\n')
arch.write('         S\n')
arch.write(' ')
arch.write('0.0')
arch.write(' ')
arch.write('%.2f' % val_trb['valor'].iloc[0])
arch.write('\n')

arch.write(' ')
arch.write('1.0E7')
arch.write(' ')
arch.write('%.2f' % val_trb['valor'].iloc[0])
arch.write('\n')

arch.close()

# Archivo para modelación anual
arch = open('Q_' + arch_name[3:-4].upper() + '.loi', 'w')
arch.write('# ' + Nombre_Archivo + '\n')
arch.write('# Temps (s) Debit\n')
arch.write('         S\n')
arch.write(' ')
arch.write('0.0')
arch.write(' ')
arch.write('%.2f' % val_trb['valor'].iloc[0])
arch.write('\n')

for i in np.arange(len(val_sec)):
    
    arch.write(' ')
    arch.write('%.1f' % (val_sec['tiempo'].iloc[i] - 86399))
    arch.write(' ')
    arch.write('%.2f' % (val_trb['valor'].iloc[i]))
    arch.write('\n')
    
    arch.write(' ')
    arch.write('%.1f' % (val_sec['tiempo'].iloc[i]))
    arch.write(' ')
    arch.write('%.2f' % (val_trb['valor'].iloc[i]))
    arch.write('\n')
arch.close()
    
## ------------ CAMBIAR NOMBRE DE ENTRADA --------------------------------------
#arch.write('# Q_Sogamoso\n')
## -----------------------------------------------------------------------------
#arch.write('# Temps (s) Debit\n')
#arch.write('         S\n')
#
#arch.write(' ')
#arch.write('0.0')
#arch.write(' ')
#arch.write('%.2f' % val_trb['valor'].iloc[0])
#arch.write('\n')
#
#for i in np.arange(len(val_sec)):
#    arch.write(' ')
#    arch.write('%.1f' % val_sec['tiempo'].iloc[i])
#    arch.write(' ')
#    arch.write('%.2f' % val_trb['valor'].iloc[i])
#    arch.write('\n')
#arch.close()
#    
