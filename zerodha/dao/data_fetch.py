from kiteconnect import KiteTicker, KiteConnect
import pandas as pd
import numpy as nm
from datetime import datetime, timedelta
import talib


if __name__ == '__main__':
    api_key = open('/Users/rupali/Python/stock-trafficker/zerodha/api_key.txt', 'r').read()
    api_secret = open('/Users/rupali/Python/stock-trafficker/zerodha/api_secret.txt', 'r').read()
    kite = KiteConnect(api_key=api_key)
    access_token = open('/Users/rupali/Python/stock-trafficker/zerodha/access_token.txt', 'r').read()

    # If already opened previously in a given day
    # kite.set_access_token(access_token)
    # If opening the access token file for the first time in a day
    print(kite.login_url())
    data = kite.generate_session(request_token='p9t0Xfc7DieAaim85MbxbkyWPZQwe9d0', api_secret=api_secret)
    print(data['access_token'])
    kite.set_access_token(data['access_token'])
    with open('/Users/rupali/Python/stock-trafficker/zerodha/access_token.txt', 'w') as at:
        at.write(data['access_token'])

    # Dates between which you want to fetch the historical data
    # Current date - 100 days
    from_date = datetime.strftime(datetime.now() - timedelta(100), '%Y-%m-%d')
    to_date = datetime.today().strftime('%Y-%m-%d')

    interval = '5minute'

    tokens = {738561: 'RELIANCE', 341249: 'HDFCBANK'}
    while True:
        # Fetch the historical data only at the end of 5 minutes - seconds should be zero and minutes should be
        # divisible by 5, remainder 0
        if (datetime.now().second == 0) and (datetime.now().minute % 5 == 0):
            for token in tokens:
                records = kite.historical_data(token, from_date=from_date, to_date=to_date, interval=interval)
                print(records)
                df = pd.DataFrame(records)
                print(df)
                df.drop(df.tail(1).index, inplace=True)

                open = df['open'].values
                high = df['high'].values
                low = df['low'].values
                close = df['close'].values
                volume = df['volume'].values

                # sma5 crossover sma20 i.e., sma5 > sma20
                sma5 = talib.SMA(close, 5)
                sma20 = talib.SMA(close, 20)

                print(sma5[-1])
                print(sma20[-1])

                # If limit order dictionary of dictionaries
                price = kite.ltp('NSE:' + tokens[token])
                ltp = price['NSE:' + tokens[token]]['last_price']
                print(ltp)

                if(sma5[-2] < sma20[-2]) and (sma5[-1] > sma20[-1]):

                    buy_order_id = kite.place_order(variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE,
                                                    order_type=kite.ORDER_TYPE_MARKET, tradingsymbol=tokens[token],
                                                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                                                    quantity=1, price=None, squareoff=10, stoploss=2,
                                                    trailing_stoploss=1, validity=kite.VALIDITY_DAY,
                                                    product=kite.PRODUCT_MIS)

                if (sma5[-2] > sma20[-2]) and (sma5[-1] < sma20[-1]):
                    buy_order_id = kite.place_order(variety=kite.VARIETY_REGULAR, exchange=kite.EXCHANGE_NSE,
                                                    order_type=kite.ORDER_TYPE_MARKET, tradingsymbol=tokens[token],
                                                    transaction_type=kite.TRANSACTION_TYPE_SELL,
                                                    quantity=1, price=None, squareoff=10, stoploss=2,
                                                    trailing_stoploss=1, validity=kite.VALIDITY_DAY,
                                                    product=kite.PRODUCT_MIS)

