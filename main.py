import pandas as pd
import plotly.graph_objects as go


def get_trades_data(file_path):
    df = pd.read_csv(file_path)
    df['TS'] = pd.to_datetime(df['TS'])
    df['Open'] = df['PRICE']
    df['High'] = df['PRICE']
    df['Low'] = df['PRICE']
    df['Close'] = df['PRICE']

    return df


def create_candlesticks(trades, interval_minutes):
    ohlc_dict = {
        'TS': 'first',
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
    }

    candlesticks = trades.resample(f'{interval_minutes}T', on='TS').apply(ohlc_dict).dropna()

    return candlesticks


def plot_candlestick(data):

    fig = go.Figure(
        data=[
            go.Candlestick(
                x=data['TS'],
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'],
                name='Candlestick'
            )
        ]
    )

    if ema_data is not None:
        fig.add_trace(go.Scatter(
            x=data['TS'],
            y=ema_data,
            mode='lines',
            name='EMA'
        ))

    fig.update_layout(
        title='Candlestick Chart',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis_rangeslider_visible=True
    )

    fig.show()


def calculate_ema(data, length):
    ema = data['Close'].ewm(span=length, adjust=False).mean()
    return ema


if __name__ == '__main__':
    csv_file = 'prices.csv'
    interval_minutes = 60
    ema_length = 90

    trades_data = get_trades_data(csv_file)

    candlesticks_data = create_candlesticks(trades_data, interval_minutes)
    ema_data = calculate_ema(data=candlesticks_data, length=ema_length)

    plot_candlestick(candlesticks_data)
