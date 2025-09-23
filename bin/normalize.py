"""Normalize Yahoo and WSJ gainer CSV files into a standard format."""

import os
import re

import pandas as pd


def normalize_yahoo(input_csv, output_csv="ygainers_normalized.csv"):
    """Normalize Yahoo gainers CSV."""
    df = pd.read_csv(input_csv)
    df['price'] = df['Price'].apply(lambda x: str(x).split()[0])
    df['change'] = df['Chg']
    df['perc_change'] = df['% Chg'].str.replace('%', '', regex=False)
    df['symbol'] = df['Symbol']
    df['company_name'] = df['Name']
    df['volume'] = df['Volume']

    out = df[['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']]
    out.to_csv(output_csv, index=False)
    return out


def normalize_wsj(input_csv, output_csv="wsjgainers_normalized.csv"):
    """Normalize WSJ gainers CSV."""
    df = pd.read_csv(input_csv)
    rex = r'\(([A-Z]+)\)$'
    df['symbol'] = df['Unnamed: 0'].apply(
        lambda x: re.findall(rex, str(x))[0] if pd.notna(x) else ''
    )
    df['company_name'] = df['Unnamed: 0'].apply(
        lambda x: re.sub(rex, '', str(x)).strip()
    )
    df['price'] = df['Last']
    df['change'] = df['Chg']
    df['perc_change'] = df['% Chg']
    df['volume'] = df['Volume']

    out = df[['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']]
    out.to_csv(output_csv, index=False)
    return out


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
