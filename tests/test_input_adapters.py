import os
import unittest

import pandas as pd

from exceptions import IncorrectDataException
from input_adapters import CsvInputAdapter


class CsvInputAdapterTest(unittest.TestCase):
    def test_get_dataframe_correct_data(self):
        temp_csv_file = 'test_data.csv'
        data = {
            'TS': [
                '2023-01-01 00:00:00',
                '2023-01-01 00:10:00',
                '2023-01-01 00:20:00'
            ],
            'PRICE': [100, 105, 110]
        }
        df = pd.DataFrame(data)
        df.to_csv(temp_csv_file, index=False)

        adapter = CsvInputAdapter(temp_csv_file)
        result_df = adapter.get_dataframe(interval_minutes=10)

        self.assertTrue('TS' in result_df.columns)
        self.assertTrue('Open' in result_df.columns)
        self.assertTrue('High' in result_df.columns)
        self.assertTrue('Low' in result_df.columns)
        self.assertTrue('Close' in result_df.columns)
        self.assertEqual(len(result_df), 3)

        os.remove(temp_csv_file)

    def test_get_dataframe_incorrect_data(self):
        temp_csv_file = 'test_data.csv'
        data = {
            'TS': ['2023-01-01 00:00:00', '2023-01-01 00:10:00', 'invalid_date'],
            'PRICE': [100, 105, 'invalid_price']
        }
        df = pd.DataFrame(data)
        df.to_csv(temp_csv_file, index=False)

        adapter = CsvInputAdapter(temp_csv_file)

        with self.assertRaises(IncorrectDataException):
            adapter.get_dataframe(interval_minutes=10)

        os.remove(temp_csv_file)

    def test_get_dataframe_invalid_file_format(self):
        temp_txt_file = 'test_data.txt'
        with open(temp_txt_file, 'w') as file:
            file.write(
                'TS,PRICE\n2023-01-01 00:00:00,100\n'
                '2023-01-01 00:10:00,105\n2023-01-01 00:20:00,110'
            )

        with self.assertRaises(ValueError):
            CsvInputAdapter(temp_txt_file)

        os.remove(temp_txt_file)
