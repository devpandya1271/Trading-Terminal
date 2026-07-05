from binance import ThreadedWebsocketManager
import transformer
import api

class BinanceWebSocket:
    def __init__(self,market):
        self.market = market
        self.websocket_manager = None
        self.connected = False

    def start(self):
        api_key,api_secret = api.get_binance_api
        self.websocket_manager = ThreadedWebsocketManager(
            api_key=api_key,
            api_secret=api_secret
        )

        self.websocket_manager.start()

        self.websocket_manager.start_kline_socket(
            callback=self.stream_candle,
            symbol= self.market.symbol,
            interval=self.market.timeframe
        )

        self.connected = True


    def stream_candle(self,msg):

        candle = transformer.transform_binance_candle(msg)

        self.market.update_candle(candle)


        

