import pandas as pd 

def read_df(path): 
    df = pd.read_csv(path, sep=',')

    df['Date'] = pd.to_datetime(
        df['Date']
    )
    return df

def clean_dataset(df): 

    columns_remove = [

        # información del partido
        'Div',
        'Date',
        'Time',

        # fuga de información
        'HomeResult',
        'AwayResult',
        'HomePoints',
        'AwayPoints',
        'HomeWin',
        'AwayWin',

        # goles del partido actual
        'HomeGoalsFor',
        'AwayGoalsFor',
        'HomeGoalsAgainst',
        'AwayGoalsAgainst'
    ]

    df = df.drop(
        columns=columns_remove
    )

    return df  

def split_dataset(df): 

    y = df['FTR']

    X = df.drop(
        columns=['FTR']
    )

    X = clean_dataset(X)

    return X, y

def main(): 
    path = 'match-predictor/data/processed/italy/Season 2024-2025/I1_features.csv'
    df = read_df(path)
    print(df['Date'].min())
    print(df['Date'].max())
    print(df.columns.tolist())
    X, y = split_dataset(df)
    print(X.shape)
    print(y.shape)

    print(X.dtypes.value_counts())
    print(y.value_counts())
    

main()
