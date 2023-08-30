from typing import Optional, List

import plotly.graph_objects as go
from pandas import DataFrame

from indicators import AbstractIndicator


class CandlestickPlot:
    def __init__(
            self,
            plot_data: DataFrame,
            name: str = 'Candlestick',
            indicators: Optional[List[AbstractIndicator]] = None
    ):
        self.plot_data = plot_data
        self.name = name
        self.indicators = indicators

    def show(self):
        fig = go.Figure(
            data=[
                go.Candlestick(
                    x=self.plot_data['TS'],
                    open=self.plot_data['Open'],
                    high=self.plot_data['High'],
                    low=self.plot_data['Low'],
                    close=self.plot_data['Close'],
                    name='Price'
                )
            ]
        )
        if self.indicators:
            for indicator in self.indicators:
                fig.add_trace(indicator.build())

        fig.update_layout(
            title=self.name,
            xaxis_title='Date',
            yaxis_title='Price',
            xaxis_rangeslider_visible=True
        )

        fig.show()
