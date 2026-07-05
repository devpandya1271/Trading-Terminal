from gui.renderers.candlestick_renderer import CandlestickRenderer
from gui.transform.chart_transform import ChartTransform

class ChartEngine:

    def __init__(self,chart,market):

        self.chart = chart
        self.market = market 

        self.transform = ChartTransform(self.market)

        self.renderers = []

        self.renderers.append(
            CandlestickRenderer(
                chart=self.chart,
                market=self.market,
                transform=self.transform
            )
        )

    def draw(self):

        print("ChartEngine.draw()")

        for renderer in self.renderers:
            renderer.draw()

