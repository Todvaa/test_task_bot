from abc import ABC, abstractmethod

import pandas as pd
from pandas import DataFrame


class InputAdapterInterface(ABC):
    FILE_EXTENSION = None

    def __init__(self, file_path: str):
        if not file_path.endswith(self.FILE_EXTENSION):
            raise ValueError('Invalid file extension. Only .csv files are allowed.')

        self.file_path = file_path

    @abstractmethod
    def run(self, interval_minutes: int) -> DataFrame:
        pass


class CsvInputAdapter(InputAdapterInterface):
    FILE_EXTENSION = '.csv'
    OHLC_DICT = {
        'TS': 'first',
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
    }

    def run(self, interval_minutes: int) -> DataFrame:
        df = pd.read_csv(self.file_path)
        df['TS'] = pd.to_datetime(df['TS'])
        df['Open'] = df['PRICE']
        df['High'] = df['PRICE']
        df['Low'] = df['PRICE']
        df['Close'] = df['PRICE']

        return df.resample(
            f'{interval_minutes}T', on='TS'
        ).apply(self.OHLC_DICT).dropna()
