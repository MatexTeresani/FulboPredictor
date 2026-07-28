import pandas as pd 
import groupby_practice 
    
def create_columnsHome(newdf, df):
        
    newdf['Date'] = df['Date']
    newdf['Team'] = df['HomeTeam']
    newdf['Opponent'] = df['AwayTeam']
    newdf['GoalsFor'] = df['FTHG']
    newdf['GoalsAgainst'] = df['FTAG']
    newdf['Result'] = df['FTR'].map({
        'H': 'W', 
        'D': 'D',
        'A': 'L'
    })
    
    return newdf

def create_columnsAway(newdf, df):
        
    newdf['Date'] = df['Date']
    newdf['Team'] = df['AwayTeam']
    newdf['Opponent'] = df['HomeTeam']
    newdf['GoalsFor'] = df['FTAG']
    newdf['GoalsAgainst'] = df['FTHG']
    newdf['Result'] = df['FTR'].map({
        'A': 'W', 
        'D': 'D', 
        'H': 'L'
    })
    
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
    history['Points'] = history['Result'].map({
        'W': 3, 
        'D': 1,
        'L': 0
    })
    history['AvgPointsLast3'] = history.groupby('Team')['Points'].transform(lambda x: x.shift(1).rolling(3).mean())
    history['AvgGoalsForLast3'] = history.groupby('Team')['GoalsFor'].transform(lambda x: x.shift(1).rolling(3).mean())
    history['AvgGoalsAgainstLast3'] = history.groupby('Team')['GoalsAgainst'].transform(lambda x: x.shift(1).rolling(3).mean())
    history['Win'] = history['Result'].map({
        'W': 1,
        'D': 0,
        'L': 0
    })
    history['WinLast3'] = history.groupby('Team')['Win'].transform(lambda x: x.shift(1).rolling(3).sum())
    history['GoalDiferenceLast3'] = history['AvgGoalsForLast3'] - history['AvgGoalsAgainstLast3']

    print(history.head())
    print(history.shape)
    
main()    