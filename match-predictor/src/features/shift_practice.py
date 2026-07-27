import pandas as pd 
import groupby_practice 

def main():
    path = 'match-predictor\data\processed\italy\Season 2024-2025\I1_processed.csv'
    df = groupby_practice.read_df(path)
    df = df.sort_values(by='Date').reset_index(drop=True)
    df['PreviousHomeGoals'] = df.groupby('HomeTeam')['FTHG'].shift(1)
    df['AvgHomeGoalsLast3'] = df.groupby('HomeTeam')['FTHG'].transform(lambda x: x.shift(1).rolling(3).mean())
    df['AvgHomeGoalsConcededLast3'] = df.groupby('HomeTeam')['FTAG'].transform(lambda x: x.shift(1).rolling(3).mean())
    df['PreviousAwayGoals'] = df.groupby('AwayTeam')['FTAG'].shift(1)
    df['AvgAwayGoalsLast3'] = df.groupby('AwayTeam')['FTAG'].transform(lambda x: x.shift(1).rolling(3).mean())
    df['AvgAwayGoalsConcededLast3'] = df.groupby('AwayTeam')['FTHG'].transform(lambda x: x.shift(1).rolling(3).mean())
    juventus = df[df['HomeTeam'] == 'Juventus'].copy()
    juventus = juventus.sort_values(by='Date').reset_index(drop=True)
    
    juventus['PreviousGoals'] = juventus['FTHG'].shift(1)
    juventus['AvgGoalsLast3'] = juventus['PreviousGoals'].rolling(3).mean()
    
    print(juventus[['Date', 'HomeTeam', 'PreviousGoals']])
    print(
        df[
            [
                'Date',
                'HomeTeam',
                'FTHG',
                'AvgHomeGoalsLast3'
            ]
        ].head(20)
)
main()