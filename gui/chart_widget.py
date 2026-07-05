from math import fabs
from PySide6.QtWidgets import QWidget, QVBoxLayout
import pyqtgraph as pg

from gui.chart_engine import ChartEngine


class ChartWidget(QWidget):
    def __init__(self,market):
        super().__init__()

        self.market = market

        self.layout = QVBoxLayout()

        self.chart = pg.PlotWidget()

        self.chart.hideButtons()

        self.chart.showGrid(x=False, y=False)
        self.chart.setBackground('black')

        self.engine = ChartEngine( 
            self.chart,
            self.market
        )

        self.engine.transform.set_chart_size(
            self.chart.width(),
            self.chart.height()
        )

        self.layout.addWidget(self.chart)

        self.setLayout(self.layout)

        self.engine.draw()
       


    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.engine.transform.set_chart_size(
            self.chart_width(),
            self.chart_heigh()
        )

        self.engine.draaw()