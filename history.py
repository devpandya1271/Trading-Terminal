import api
import transformer




##Binance
def get_binance_ohlcv_history(symbol, timeframe, start, end = None):

    binance_client = api.get_binance_client()
    
    bars = binance_client.get_historical_klines(

        symbol=symbol,
        interval=timeframe,
        start_str=start,
        end_str=end,
        limit=1000
    )

    return transformer.binance_dataframe(bars)


##CCXT
def get_ccxt_ohlcv_history(symbol, timeframe, start, limit=1000):

    ccxt_client = api.get_ccxt_client()

    start = ccxt_client.parse8601(start)
    data = ccxt_client.fetch_ohlcv(

        symbol=symbol,
        timeframe=timeframe,
        since=start,
        limit=limit
    )

    return transformer.ccxt_dataframe(data)


