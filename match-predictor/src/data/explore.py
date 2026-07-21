import pandas as pd 

ROUTE = r'match-predictor\data\raw\italy\Season 2024-2025\I1.csv'

def reader(route): 
    df = pd.read_csv(route)
    
    return df 

df = reader(ROUTE)

print(df.head()) # columnas y primeras 5 filas 
print(df.shape) # cantidad de filas y de colmnas 
print(df.columns) # columnas 
print(df.info()) # datos del csv, columnas datatypes, uso de memoria 
print(df.isnull().sum()) # datos nulos 
print(df.describe()) # mas datos para usar mas adelante para el modelo
'''
Div        Date   Time    HomeTeam   AwayTeam  FTHG  FTAG  ... B365CAHA  PCAHH  PCAHA MaxCAHH  MaxCAHA  AvgCAHH  AvgCAHA
'''
'''
archivo  fecha hora equipo local equipo visitante golesE1 golesE2 .... estadisticas durante el paritda ( analizar mas adelante)
'''
