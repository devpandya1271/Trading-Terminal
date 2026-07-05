from PySide6.QtWidgets import QMainWindow
from gui.chart_widget import ChartWidget

class MainWindow(QMainWindow):
    def __init__(self,market):
        super().__init__()

        self.setWindowTitle("TradingTerminal")
        self.resize(1400,900)


        self.chart_widget = ChartWidget(market)
        self.setCentralWidget(self.chart_widget)
        