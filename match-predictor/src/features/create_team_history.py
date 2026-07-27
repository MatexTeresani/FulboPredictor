import pandas as pd 
import groupby_practice 
    
def create_columnsHome(newdf, df):
        
    newdf['Date'] = df['Date']
    newdf['Team'] = df['HomeTeam']
    newdf['Opponent'] = df['AwayTeam']
    newdf['GoalsFor'] = df['FTHG']
    newdf['GoalsAgainst'] = df['FTAG']
    
    return newdf

def create_columnsAway(newdf, df):
        
    newdf['Date'] = df['Date']
    newdf['Team'] = df['AwayTeam']
    newdf['Opponent'] = df['HomeTeam']
    newdf['GoalsFor'] = df['FTAG']
    newdf['GoalsAgainst'] = df['FTHG']
    
    return newdf
def concat_df(df1, df2): 
    
    history = pd.concat(
        [df1, df2], 
        ignore_index=True
    )
    return history 

def order_concat(history): 
    history = history.sort_values(by=['Team', 'Date'])
    return history 

def main(): 
    path = 'match-predictor\data\processed\italy\Season 2024-2025\I1_processed.csv'
    df = groupby_practice.read_df(path)
    home = pd.DataFrame()
    away = pd.DataFrame()
    home = create_columnsHome(home, df)
    away = create_columnsAway(away, df)
    history = concat_df(home, away)
    history = order_concat(history)
    
    print(history.head())
    print(history.shape)
    
main()    