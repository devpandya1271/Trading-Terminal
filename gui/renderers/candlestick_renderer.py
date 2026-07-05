from .base_renderer import BaseRenderer
from gui.items.candlestick_item import CandlestickItem

class CandlestickRenderer(BaseRenderer):

    def __init__(self, chart, market,transform):
        super().__init__(chart, market)

        self.transform = transform

        self.item = CandlestickItem(
            self.market.ohlcv_data,
            self.transform
        )

        self.chart.addItem(self.item)

        print('Items added to chart')


    def draw(self):

        print("Renderer draw")

        self.item.update_data(self.market.ohlcv_data)
        


