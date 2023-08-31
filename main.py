import os
import urllib

from configs import configure_manager
from input_adapters import AVL_INPUT_ADAPTERS
from plots import CandlestickPlot
from exceptions import InputStringException
from indicators import Ema


def match_input(input: str):
    """Searches for a matching adapter for the input data"""
    if urllib.parse.urlparse(input).scheme:
        raise InputStringException('Data download links are not supported yet')

    if not os.path.isfile(input):
        raise InputStringException('The file was not found at the specified path')

    file_extension = os.path.splitext(input)[-1]
    for input_adapter in AVL_INPUT_ADAPTERS:
        if file_extension == input_adapter.FILE_EXTENSION:
            return input_adapter(file_path=input)
    raise InputStringException(
        f'{input} is not supported, specify'
        f' a file with a valid extension '
        f'{[adapter.FILE_EXTENSION for adapter in AVL_INPUT_ADAPTERS]}'
        f' or a link to download the data.'
    )


def main():
    """Main function of the project"""
    plot_manager = configure_manager()
    args = plot_manager.parse_args()

    input_adapter = match_input(input=args.input)
    plot_data = input_adapter.get_dataframe(interval_minutes=args.interval_minutes)

    indicators = []
    if args.ema:
        indicators.append(Ema(plot_data=plot_data, period=args.ema))

    CandlestickPlot(plot_data=plot_data, indicators=indicators).show()


if __name__ == '__main__':
    main()
