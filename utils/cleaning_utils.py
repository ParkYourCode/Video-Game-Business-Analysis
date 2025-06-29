import pandas as pd

def extract_lookup_table(df, col_name):
    col_vals = df[col_name].dropna().unique()
    return pd.DataFrame({col_name: col_vals})

def extract_columns_into_table(df, cols):
    return df[cols].copy()

def drop_columns(df, cols):
    return df.drop(columns=cols)