class BaseRenderer:
    def __init__(self,chart,market):

        self.chart = chart
        self.market = market 

    def draw(self):
        raise NotImplementedError