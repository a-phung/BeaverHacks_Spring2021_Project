import pandas as pd
import yfinance as yf
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

msft = yf.Ticker("MSFT")
print(msft)