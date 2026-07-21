import pandas as pd 
import os 

def load_data(path): 
    df = pd.read_csv(path, sep=',')
    
    return df 

def convert_dates(df): 
    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
    
    return df 

def sort_matches(df): 
    df = df.sort_values(
        by='Date', 
        ascending=True
        
        )
    
    return df

def reset_dataframe(df): 
    df = df.reset_index(
        drop=True 
    )

    return df 
    
def remove_duplicates(df): 
    df = df.drop_duplicates(
        subset = ['Date', 'HomeTeam', 'AwayTeam'], 
        keep = 'first' 
    )
    
    return df 
def save_processed(df, path): 
    route = os.path.dirname(path)
    
    if route: 
        os.makedirs(route, exist_ok=True)

    df.to_csv(
        path,
        index=False
    )

def main(): 
    ROUTE = r'match-predictor\data\raw\italy\Season 2024-2025\I1.csv'
    saveRoute = r'match-predictor\data\processed\italy\Season 2024-2025\I1_processed.csv'
    df = load_data(ROUTE)
    print(df.info())
    df = convert_dates(df)
    df = sort_matches(df)
    df = reset_dataframe(df)
    df = remove_duplicates(df)
    
    save_processed(df, saveRoute)

    
main()
    
    