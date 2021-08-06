import pyfolio as pf
import pandas as pd
import yfinance as yf


if __name__ == '__main__':
   # Define the ticker list
  tickers_list = ['AAPL', 'AMZN', 'MSFT', 'WMT']
  # Import pandas and create a placeholder for the data
  data = pd.DataFrame(columns=tickers_list)
  # Feth the data
  for ticker in tickers_list:
   data[ticker] = yf.download(ticker, period='5y',)['Adj Close']
  # Compute the returns of individula stocks and then compute the daily mean returns.
  # The mean return is the daily portfolio returns with the above four stocks.
  data = data.pct_change().dropna().mean(axis=1)
  # Print first 5 rows of the data
  print(data.head())
  # fig = pf.create_full_tear_sheet(data) ##TODO : Why not working
  # pf.create_position_tear_sheet(data)
  # pf.create_returns_tear_sheet(data)
  fig = pf.create_returns_tear_sheet(data, return_fig=True)
  fig.savefig('/Users/rupali/Python/stock-trafficker/yahoo_finance/controllers/returns_tear_sheet.pdf')