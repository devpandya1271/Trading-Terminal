
class ChartTransform():

    def __init__(self,market):

        self.market = market


        self.candle_width = 12
        self.candle_spacing = 2
        self.chart_height = 0
        self.chart_width = 0 

    def set_chart_size(self,width, height):

        self.chart_height = height
        self.chart_width = width 

    def max_price(self):
        return self.market.ohlcv_data["High"].max()

    def min_price(self):

        return self.market.ohlcv_data["Low"].min()

    def index_to_x(self,index):

        return index *(
            self.candle_width+self.candle_spacing
            )

    def price_to_y(self,price):

        max_price = self.max_price()
        min_price = self.min_price()

        normalized = (
            price - min_price
        )/(max_price - min_price
        )
        

        return self.chart_height * (
            1 - normalized
        )