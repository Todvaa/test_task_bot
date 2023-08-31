from abc import ABC, abstractmethod

import pandas as pd

from exceptions import IncorrectDataException


class AbstractInputAdapter(ABC):
    """Abstract class for adapters"""
    FILE_EXTENSION = None

    def __init__(self, file_path: str):
        if not file_path.endswith(self.FILE_EXTENSION):
            raise ValueError(
                f'Invalid file extension.'
                f' Only {self.FILE_EXTENSION} files are allowed.'
            )

        self.file_path = file_path

    @abstractmethod
    def get_dataframe(self, interval_minutes: int) -> pd.DataFrame:
        pass


class CsvInputAdapter(AbstractInputAdapter):
    """Adapter for csv files"""
    FILE_EXTENSION = '.csv'
    OHLC_DICT = {
        'TS': 'first',
        'Open': 'first',
        'High': 'max',
        'Low': 'min',
        'Close': 'last',
    }

    def _resample_data(
            self, df: pd.DataFrame, interval_minutes: int
    ) -> pd.DataFrame:
        return df.resample(
            f'{interval_minutes}T', on='TS'
        ).apply(self.OHLC_DICT).dropna()

    def get_dataframe(self, interval_minutes: int) -> pd.DataFrame:
        try:
            df = pd.read_csv(self.file_path)
            df['TS'] = pd.to_datetime(df['TS'])
            df['Open'] = df['PRICE']
            df['High'] = df['PRICE']
            df['Low'] = df['PRICE']
            df['Close'] = df['PRICE']

            return self._resample_data(df, interval_minutes)
        except Exception as e:
            raise IncorrectDataException(f'An error occurred while reading data: {str(e)}')


AVL_INPUT_ADAPTERS = (CsvInputAdapter,)
