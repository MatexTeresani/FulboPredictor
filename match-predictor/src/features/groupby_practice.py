import pandas as pd 

def read_df(path): 
    df = pd.read_csv(path, sep=',')
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

    return df 

def main(): 
    path = 'match-predictor/data/raw/italy/Season 2024-2025/I1.csv'
    df = read_df(path)
    
    promHome = df.groupby('HomeTeam')['FTHG'].mean()
    promVisit = df.groupby('AwayTeam')['FTAG'].mean()
    homeMatches = df.groupby('HomeTeam').size()
    
    print(promHome)
    print(promVisit)
    print(homeMatches)
main()