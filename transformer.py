import pandas as pd


def binance_dataframe(bars):

    df = pd.DataFrame(bars)

    df["Date"] = pd.to_datetime(df.iloc[:, 0], unit="ms")

    df.columns = [
        "Open Time",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume",
        "Close Time",
        "Quote Asset Volume",
        "Number of Trades",
        "Taker Buy Base Asset Volume",
        "Taker Buy Quote Asset Volume",
        "Ignore",
        "Date"
    ]

    df = df[
        ["Date", "Open", "High", "Low", "Close", "Volume"]
    ].copy()

    df.set_index("Date", inplace=True)

    numeric_cols = ["Open", "High", "Low", "Close", "Volume"]
    df[numeric_cols] = df[numeric_cols].astype(float)

    return df


def ccxt_dataframe(data):

    df = pd.DataFrame(
        data,
        columns=[
            "Date",
            "Open",
            "High",
            "Low",
            "Close",
            "Volume"
        ]
    )

    df["Date"] = pd.to_datetime(df["Date"], unit="ms")

    df.set_index("Date", inplace=True)

    return df.astype(float)

def transform_binance_candle(msg):
    candle : {
        "event_time" : pd.to_datetime(msg["E"], unit = "ms"),
        "start_time" : pd.to_datetime(msg["k"]["t"], unit = "ms"),
        "first"   : float(msg["k"]["o"]),
        "high"    : float(msg["k"]["h"]),
        "low"     : float(msg["k"]["l"]),
        "close"   : float(msg["k"]["c"]),
        "volume"  : float(msg["k"]["v"]),
        "complete":       msg["k"]["x"],
    }

    return candle
    
