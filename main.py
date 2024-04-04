import pandas as pd
import yfinance as yf
from datetime import datetime

# Read Excel file with pandas (skips first row)
symbol_list_ibrx = pd.read_excel("files/ibr.xlsx", skiprows=1)["Código"].values

# Empty DataFrame to store scan results
df_scan = pd.DataFrame(columns=["Dividend Yield"])

# Stock symbol iteration
for ativo in symbol_list_ibrx:
    # Retrieve data for the current stock
    stock_history = yf.Ticker(f"{ativo}.SA").history(period="36mo")
    
    # Calculate dividends received in the last two years
    dividends_sum = stock_history["Dividends"].fillna(0).loc[str(datetime.now().year - 1) :].sum()
    
    # Calculate dividend yield
    last_close = stock_history["Close"].iloc[-1]
    dividend_yield = ((dividends_sum/2) / last_close) * 100
    
    # Append the calculated dividend yield to the df_scan DataFrame
    df_scan.loc[ativo] = dividend_yield

# Sort the DataFrame by dividend yield in descending order and display the top 20 stocks
top_20_dividend_yield = df_scan.sort_values(by="Dividend Yield", ascending=False).head(20)
print(top_20_dividend_yield)