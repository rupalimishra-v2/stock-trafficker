from datetime import date
from nsepy import get_history
import matplotlib.pyplot as plt

if __name__ == '__main__':

 # Stock options (for index options, set index = True)
 stock_fut = get_history(symbol="HDFC",
  start=date(2019, 1, 15),
  end=date(2019, 2, 1),
  futures=True,
  expiry_date=date(2019, 2, 28))
 stock_fut.head()

 stock_fut.Close.plot(figsize=(10, 5))
 # Define the label for the title of the figure
 plt.title("Close Price", fontsize=16)
 # Define the labels for x-axis and y-axis
 plt.ylabel('Price', fontsize=14)
 plt.xlabel('Date', fontsize=14)
 # Plot the grid lines
 plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
 plt.show()

 # Options data
 stock_opt = get_history(symbol="HDFC",
                         start=date(2019, 1, 15),
                         end=date(2019, 2, 1),
                         option_type="CE",
                         strike_price=2000,
                         expiry_date=date(2019, 2, 28))
 stock_opt.head()