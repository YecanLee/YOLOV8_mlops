import pandas as pd
import os

directory = '/Users/.../data'
def concatenate_dataframes(directory):
    files = [f for f in os.listdir(directory) if f.endswith('.csv')] 
    dfs = [pd.read_csv(os.path.join(directory, f)) for f in files]
    concatenated_df = pd.concat(dfs, ignore_index=True)
    return concatenated_df

concatenated_df = concatenate_dataframes(directory)
