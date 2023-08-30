import argparse


def configure_manager():
    manager = argparse.ArgumentParser(
        description='Building a price plot'
    )
    manager.add_argument(
        'input_string',
        help='Link or file path with an extension',
    )
    manager.add_argument(
        'interval_minutes',
        type=int,
        help='Desired timeframe in minutes',
    )
    manager.add_argument(
        '-e',
        '--ema',
        type=int,
        help=(
            'Adds an exponential moving average of'
            ' the specified period to the chart'
        )
    )

    return manager
