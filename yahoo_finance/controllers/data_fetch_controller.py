
from pandas_datareader import data
import matplotlib.pyplot as plt
import yfinance as yf


# Set the start and end date
if __name__ == '__main__':
    start_date = '1990-01-01'
    end_date = '2019-02-01'
    # Set the ticker
    ticker = 'AAPL'
    # Get the data
    data = data.get_data_yahoo(ticker, start_date, end_date)
    # print(data.head())

    # Plot the adjusted close price
    data['Adj Close'].plot(figsize=(10, 7))
    # Define the label for the title of the figure
    plt.title("Adjusted Close Price of %s" % ticker, fontsize=16)
    # Define the labels for x-axis and y-axis
    plt.ylabel('Price', fontsize=14)
    plt.xlabel('Year', fontsize=14)
    # Plot the grid lines
    plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
    # Show the plot
    plt.show()
