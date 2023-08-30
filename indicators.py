from abc import ABC, abstractmethod

from pandas import DataFrame
import plotly.graph_objects as go
from plotly.graph_objs import Scatter


class AbstractIndicator(ABC):
    @abstractmethod
    def build(self):
        pass


class Ema(AbstractIndicator):
    def __init__(self, plot_data: DataFrame, period: int):
        self.plot_data = plot_data
        self.period = period

    def __calculate_ema(self):
        return self.plot_data['Close'].ewm(span=self.period, adjust=False).mean()

    def build(self) -> Scatter:
        return go.Scatter(
            x=self.plot_data['TS'],
            y=self.__calculate_ema(),
            mode='lines',
            name='EMA'
        )


