from nt import close
import pyqtgraph as pg
from PySide6.QtCore import QRectF,Qt
from PySide6.QtGui import QPen,QBrush

from gui import transform



class CandlestickItem(pg.GraphicsObject):

    def __init__(self, ohlcv_data,transform):
        super().__init__()
        self.ohlcv_data = ohlcv_data
        self.transform = transform

    def boundingRect(self):
        width = (len(self.ohlcv_data) *
        (self.transform.candle_width +self.transform.candle_spacing)
        )

        return QRectF(
            0,0,width,self.transform.chart_height
        )

    def paint(self, painter, option, widget):

        try:
            print("Painting...")
            for i, candle in enumerate(self.ohlcv_data.itertuples()):
                self.draw_wick(
                    painter,
                    i,
                    candle.High,
                    candle.Low,
                )

                self.draw_body(
                    painter,
                    i,
                    candle.Open,
                    candle.Close
                )
        except Exception as e:
            import traceback
            traceback.print_exc()

    def draw_wick(self, painter , x, high, low):
        
        painter.setPen(QPen(Qt.red,2))

        x = self.transform.index_to_x(x)

        high = self.transform.price_to_y(high)
        low = self.transform.price_to_y(low)

        painter.drawLine(
            x,
            high,
            x,
            low
        )

    def draw_body(self, painter, x, open_price, close_price):

        if close_price >= open_price:

            pen = QPen(Qt.green, 1)
            brush = QBrush(Qt.green)

        else:

            pen = QPen(Qt.red, 1)
            brush = QBrush(Qt.red)

        painter.setPen(pen)
        painter.setBrush(brush)

        x = self.transform.index_to_x(x)

        open_y = self.transform.price_to_y(open_price)
        close_y = self.transform.price_to_y(close_price)

        top = min(open_y, close_y)
        height = abs(close_y - open_y)



        painter.drawRect(
            int(x - self.transform.candle_width/2),
            int(top),
            int(self.transform.candle_width),
            int(max(height,1))
        )


    def update_data(self, ohlcv_data):
        self.ohlcv_data = ohlcv_data
        self.update()

    