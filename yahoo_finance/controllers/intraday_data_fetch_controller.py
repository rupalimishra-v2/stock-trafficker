import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Get intraday data
    intraday_data = yf.download(tickers="MSFT",
                                period="1d",
                                interval="5m", auto_adjust=True)
    print(intraday_data.head())

    ohlcv_dict_list = intraday_data.to_dict('records')
    print(ohlcv_dict_list)

    ## TODO : Resampling to different time unit
    # for ohlcv_dict in ohlcv_dict_list:
    #     print(ohlcv_dict)
    #     intraday_data.index = pd.to_datetime(intraday_data.index)
    #
    #     intraday_data_10 = intraday_data.resample('D').agg(ohlcv_dict)
    #     print(intraday_data_10)
    #     print(intraday_data_10.head())

    # To get the fundamental data
    msft = yf.Ticker("MSFT")
    # get price to book
    pb = msft.info['priceToBook']
    pe = msft.info['regularMarketPrice'] / msft.info['epsTrailingTwelveMonths']
    print('Price to Book Ratio is: %.2f' % pb)
    print('Price to Earnings Ratio is: %.2f' % pe)
    # Revenue
    revenue = msft.financials.loc['Total Revenue']
    plt.bar(revenue.index, revenue.values)
    plt.ylabel("Total Revenues")
    plt.show()

    EBIT = msft.financials.loc['Earnings Before Interest and Taxes']
    plt.bar(EBIT.index, EBIT.values)
    plt.ylabel("EBIT")
    plt.show()

    # show income statement
    print(msft.financials)
    # show balance heet
    print(msft.balance_sheet)
    # show cashflow
    print(msft.cashflow)
    # show other info
    print(msft.info)