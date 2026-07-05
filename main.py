import sys 
from PySide6.QtWidgets import QApplication
from ccxt.base import exchange
from gui.main_window import MainWindow
from market_data import MarketData
from gui.transform.chart_transform import ChartTransform

def main():
    app = QApplication(sys.argv)
    
    

    market = MarketData(
        exchange = "BINANCE",
        symbol = "BTCUSDT",
        timeframe = '4h'
    )

    market.load_history("2026-01-01")

    print(market.ohlcv_data.tail())

    print(
        market.ohlcv_data["Close"].iloc[0] 
    )

    transform = ChartTransform(market)

    print(
        transform.price_to_y(
        market.ohlcv_data["Close"].iloc[0]
    )
    )

    window = MainWindow(market)

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()

