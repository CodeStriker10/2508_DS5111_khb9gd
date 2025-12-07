"""Tests for the OOP gainer classes."""
import sys
import os
import pandas as pd
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "bin", "gainers")))

from yahoo import GainerYahoo
from wsj import GainerWSJ


def test_yahoo_normalize():
    test_data = pd.DataFrame({
        'Symbol': ['AAPL', 'GOOGL'],
        'Name': ['Apple Inc.', 'Alphabet Inc.'],
        'Price': ['150.00', '2800.00'],
        'Change': [5.0, 50.0],
        'Change %': ['+3.45%', '+1.82%'],
        'Volume': ['1000000', '500000']
    })
    test_data.to_csv('ygainers.csv', index=False)
    
    gainer = GainerYahoo()
    result = gainer.normalize_data()
    
    expected_columns = ['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']
    assert list(result.columns) == expected_columns
    
    os.remove('ygainers.csv')
    os.remove('ygainers_normalized.csv')


def test_wsj_normalize():
    test_data = pd.DataFrame({
        'Unnamed: 0': ['Apple Inc. (AAPL)', 'Alphabet Inc. (GOOGL)'],
        'Last': [150.00, 2800.00],
        'Chg': [5.0, 50.0],
        '% Chg': [3.45, 1.82],
        'Volume': [1000000, 500000]
    })
    test_data.to_csv('wsjgainers.csv', index=False)
    
    gainer = GainerWSJ()
    result = gainer.normalize_data()
    
    expected_columns = ['symbol', 'company_name', 'price', 'change', 'perc_change', 'volume']
    assert list(result.columns) == expected_columns
    
    os.remove('wsjgainers.csv')
    os.remove('wsjgainers_normalized.csv')
