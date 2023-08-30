import os
import urllib

from configs import configure_manager
from constants import AVL_INPUT_ADAPTERS
from entities import CandlestickPlot
from exceptions import InputStringException
from indicators import Ema


def input_string_match(input_string):
    if urllib.parse.urlparse(input_string).scheme:
        raise InputStringException('Data download links are not supported yet')

    if not os.path.isfile(input_string):
        raise InputStringException('The file was not found at the specified path')

    file_extension = os.path.splitext(input_string)[-1]
    for input_adapter in AVL_INPUT_ADAPTERS:
        if file_extension == input_adapter.FILE_EXTENSION:
            return input_adapter(file_path=input_string)
    raise InputStringException(
        f'{input_string} is not supported, specify'
        f' a file with a valid extension '
        f'{[adapter.FILE_EXTENSION for adapter in AVL_INPUT_ADAPTERS]}'
        f' or a link to download the data.'
    )


def main():
    plot_manager = configure_manager()
    args = plot_manager.parse_args()

    input_adapter = input_string_match(input_string=args.input_string)
    plot_data = input_adapter.run(interval_minutes=args.interval_minutes)
    indicators = []
    if args.ema:
        indicators.append(Ema(period=args.ema, plot_data=plot_data))
    CandlestickPlot(plot_data=plot_data, indicators=indicators).show()


if __name__ == '__main__':
    main()
