import pandas as pd 
import os 

def load_processed(path): 
    df = pd.read_csv(path, sep=',')
    return df 

def dataset_info(df): 
    print(df.shape)
    print('/////////////////////////////////////')
    print(df.info())
    print('/////////////////////////////////////')
    print(df.columns)


def analyze_teams(df): 
    df_teams = pd.concat([df['HomeTeam'], df['AwayTeam']]).unique() 
    
    return df_teams 

def analyze_results(df): 
    return df['FTR'].value_counts()


def analyze_goals(df): 
    LocalGoal = df['FTHG'].mean() # mean es para el promedio 
    VisitGoal = df['FTAG'].mean()
    Goals = (sum(df['FTHG']) + sum(df['FTAG'])) / len(df)

    return LocalGoal, VisitGoal, Goals 

def main(): 
    ds = load_processed(r'match-predictor\data\processed\italy\Season 2024-2025\I1_processed.csv')    
    dataset_info(ds)
    print(ds)
    ds_teams = analyze_teams(ds)
    print(ds_teams)
    
    LocalGoal, VisitGoal, promGoals = analyze_goals(ds)
    results = analyze_results(ds)
    print(LocalGoal)
    print(VisitGoal)
    print(promGoals)
    
    
    
main()



''' para analizar '''
'''
'Date', 'Time', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR','HTHG', 'HTAG',
.............................................................................
'AvgC<2.5', 'AHCh', 'B365CAHH', 'B365CAHA', 'PCAHH', 'PCAHA', 'MaxCAHH',
'MaxCAHA', 'AvgCAHH', 'AvgCAHA'],
'''
# que significa cada uno 

# FTHG = full time home goal 
# FTAG = full time away goal 
# FTR = full time results H( gana local), D(draw, empate), A(away, visitante gana)
