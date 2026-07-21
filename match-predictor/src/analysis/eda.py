import pandas as pd 
import os 

def read_dataset(path): 
    df = pd.read_csv(path, sep=',')
    return df 


