import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#DataFrame construccion
df = pd.DataFrame([[11111,'diego'],[22222,'alejandro'],[33333,'fernanda'],[44444,'cherlyn']], index = ['a','b','c','d'], columns = ['Documento','Nombres'])

unico = df.loc['b']
print(unico)

df_copia = pd.DataFrame([{'Documento': 11111, 'nombres ': 'diego'},{'Documento': 22222, 'nombres ': 'alejandro'},{'Documento': 33333, 'nombres ': 'fernanda'},{'Documento': 44444, 'nombres ': 'cherlyn'}], index = ['a','b','c','d'], columns = ['Documento','Nombres'])

df_copy = pd.DataFrame({'Documento': [11111,22222,33333,44444], 'Nombres': ['diego','alejandro','fernanda','cherlyn'], 'edad':[12,23,24,20]}, index = ['a','b','c','d'], columns = ['Documento','Nombres'])

#cargar un csv con pandas
data = pd.read_csv('https://www.kaggle.com/hesh97/titanicdataset-traincsv')
#datos = pd.read_csv('train.csv')#archivo

#imprimir primeras filas de la data
print(data.head(5))

#imprimir ultimas rimeras filas de la data
print(data.tail(5))

#imprimir los nombres de las columnas
print(data.columns)

#imprimir la forma de la data
print(data.shape)

#imprimir analisis estadisticos
print(data.describe())

print(data['Age'].describe())

#imprimir los primeros 10 registros de 1 y 2 columnas
print(data['longitude'].head(10))
print(data[['longitude','latitude']].head(10))

#imprimir cuantos valores unicos tiene una columna
print(data.latitude.unique().shape[0])

#tipos de datos
print(data.dtypes)

#histograma de las columnas de la data
print(data.hist())
print(data['population'].hist())

#ordenar la tabla con respecto al index
print(data.sort_index(axis=0, implace=True, ascending = False))
#ordenar la tabla con respecto a las columnas
print(data.sort_index(axis=1, implace=True))
#ordenar la tabla con respecto a los valores
print(data.sort_values(by=['latitude','longitude'], inplace=True, ascending = False))

#copia de unas columnas especificas
aux = data[100:200]
aux1 = data['latitude','population'][:17000]

#imprimir una sola fila
aux = data.loc[10]

#cambiar el index de la data
fecha = pd.date_range('20200101', periods = data.shape[0])
data.index = fecha
print(data.head())

print(data.loc['20210801':'20210815', ['latitude','population']])