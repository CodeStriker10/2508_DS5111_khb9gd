import pandas as pd
import re

def normalize_yahoo(input_csv, output_csv="ygainers_normalized.csv"):
    """Normalize Yahoo gainers CSV"""
    df = pd.read_csv(input_csv)
    # Split the price string into parts (price is first part)
    df['price'] = df['Price'].apply(lambda x: str(x).split()[0])
    df['change'] = df['Chg']
    df['perc_change'] = df['% Chg'].str.replace('%', '', regex=False)
    df['symbol'] = df['Symbol']
    df['company_name'] = df['Name']
    df['volume'] = df['Volume']

    out = df[['symbol','company_name','price','change','perc_change','volume']]
    out.to_csv(output_csv, index=False)
    return out

def normalize_wsj(input_csv, output_csv="wsjgainers_normalized.csv"):
    """Normalize WSJ gainers CSV"""
    df = pd.read_csv(input_csv)
    # Extract ticker symbol from strings like "QMMM Holdings Ltd. Cl A (QMMM)"
    rex = r'\(([A-Z]+)\)$'
    df['symbol'] = df['Unnamed: 0'].apply(lambda x: re.findall(rex, str(x))[0] if pd.notna(x) else '')
    df['company_name'] = df['Unnamed: 0'].apply(lambda x: re.sub(rex, '', str(x)).strip())
    df['price'] = df['Last']
    df['change'] = df['Chg']
    df['perc_change'] = df['% Chg']
    df['volume'] = df['Volume']

    out = df[['symbol','company_name','price','change','perc_change','volume']]
    out.to_csv(output_csv, index=False)
    return out

import os

if __name__ == "__main__":
    if os.path.exists("ygainers.csv"):
        print("Normalizing Yahoo...")
        normalize_yahoo("ygainers.csv")
    else:
        print("Skipping Yahoo — file not found.")

    if os.path.exists("wsjgainers.csv"):
        print("Normalizing WSJ...")
        normalize_wsj("wsjgainers.csv")
    else:
        print("Skipping WSJ — file not found.")

    print("Done.")
