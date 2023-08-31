import unittest

import pandas as pd
from parameterized import parameterized
import plotly.graph_objects as go

from indicators import Ema


def get_sample_data():
    data = [
        {
            'TS': [], 'Close': []
        },
        {
            'TS': pd.date_range(start='2023-01-01', periods=10, freq='D'),
            'Close': [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
        },
        {
            'TS': pd.date_range(start='2023-01-01', periods=5, freq='D'),
            'Close': [125, 130, 135, 140, 145]
        }
    ]
    results = [
        [],
        [
            100.0, 102.5, 106.25, 110.625, 115.3125, 120.15625,
            125.078125, 130.0390625, 135.01953125, 140.009765625
        ],
        [
            130.01953125, 100.0, 102.5, 106.25, 110.625
        ]
    ]
    yield pd.DataFrame(data[0]), results[0], True
    yield pd.DataFrame(data[1]), results[1], True
    yield pd.DataFrame(data[2]), results[2], False


class EmaTest(unittest.TestCase):
    @parameterized.expand(get_sample_data())
    def test_ema_calculation(self, data, result, success):
        ema = Ema(data, period=3)

        ema_values = ema._Ema__calculate_ema()
        self.assertEqual(ema_values.tolist() == result, success)

    def test_build_method_returns_scatter(self):
        ema = Ema(pd.DataFrame({'TS': [], 'Close': []}), period=1)

        scatter = ema.build()

        self.assertIsInstance(scatter, go.Scatter)
