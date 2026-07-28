import pandas as pd 
import groupby_practice 
import os 

def create_columnsHome(newdf, df):
        
    newdf['Date'] = df['Date']
    newdf['Date'] = pd.to_datetime(newdf['Date'])
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
    newdf['Date'] = pd.to_datetime(newdf['Date'])
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

def create_matches_features(matches, home_history, away_history): 

    matches_features = matches.copy()

    matches_features = matches_features.merge(
        home_history,
        on=[
            'Date',
            'HomeTeam'
        ],
        how ='left'
    )

    matches_features = matches_features.merge(
        away_history, 
        on=[
            'Date',
            'AwayTeam'
        ],
        how='left'
    )

    return matches_features

def main(): 
    path = 'match-predictor/data/raw/italy/Season 2024-2025/I1.csv'
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
    history['GoalDifferenceLast3'] = history['AvgGoalsForLast3'] - history['AvgGoalsAgainstLast3']
    history['DaysSinceLastMatch'] = history.groupby('Team')['Date'].diff()
    

    home_history = history.copy()
    away_history = history.copy()

    home_history = home_history.rename(
        columns={
            'Team': 'HomeTeam',
            'Opponent': 'HomeOpponent',
            'GoalsFor': 'HomeGoalsFor',
            'GoalsAgainst': 'HomeGoalsAgainst',
            'Result': 'HomeResult',
            'Points': 'HomePoints',
            'AvgPointsLast3': 'HomeAvgPointsLast3',
            'AvgGoalsForLast3': 'HomeAvgGoalsForLast3',
            'AvgGoalsAgainstLast3': 'HomeAvgGoalsAgainstLast3',
            'GoalDifferenceLast3': 'HomeGoalDifferenceLast3',
            'DaysSinceLastMatch': 'HomeDaysSinceLastMatch',
            'Win': 'HomeWin',
            'WinLast3': 'HomeWinLast3'
    }
    )

    away_history = away_history.rename(
        columns={
            'Team': 'AwayTeam',
            'Opponent': 'AwayOpponent', 
            'GoalsFor': 'AwayGoalsFor', 
            'GoalsAgainst': 'AwayGoalsAgainst', 
            'Result': 'AwayResult',
            'Points': 'AwayPoints',
            'AvgPointsLast3': 'AwayAvgPointsLast3',
            'AvgGoalsForLast3': 'AwayAvgGoalsForLast3',
            'AvgGoalsAgainstLast3': 'AwayAvgGoalsAgainstLast3', 
            'GoalDifferenceLast3': 'AwayGoalDifferenceLast3',
            'DaysSinceLastMatch': 'AwayDaysSinceLastMatch',
            'Win': 'AwayWin',
            'WinLast3': 'AwayWinLast3'
        }
    )

    matches_features = create_matches_features(df, home_history, away_history)

    matches_features.to_csv(
        'match-predictor/data/processed/italy/Season 2024-2025/I1_features.csv',
        index=False
    )

    print(matches_features.head())
    print(matches_features.shape)
    print(matches_features.info())
    print(matches_features.isnull().sum())


main()    