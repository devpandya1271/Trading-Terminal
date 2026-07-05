import history
import transformer


class MarketData:

    def __init__(self,exchange,symbol,timeframe):
        self.exchange = exchange.lower()
        self.symbol = symbol
        self.timeframe = timeframe
        self.ohlcv_data = None

    def load_history(self,start,end=None):
        

        if self.exchange == "binance":
            self.ohlcv_data = history.get_binance_ohlcv_history(
                self.symbol,
                self.timeframe,
                start,
                end

            )
            
        elif self.exchange == "ccxt":
            self.ohlcv_data = history.get_ccxt_ohlcv_history(
                self.symbol,
                self.timeframe,
                start,
            )

        else:
            raise ValueError(f"Unsupported exchange: {self.exchange}")
        
        return self.ohlcv_data

    def update_candle(self, candle):

        self.ohlcv_data.loc[candle["start_time"]] = [
            candle["open"],
            candle["high"],
            candle["low"],
            candle["close"],
            candle["volume"]
        ]

    

