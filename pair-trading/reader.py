import pandas as pd
import pandas_datareader.data as web

import warnings


def sp500_constitutes(fname='sp500.txt'):
    """Get list of S&P500 constitutes.

    Parameters
    ----------
    fname: str
        Filename to text

    Returns
    -------
    constitutes: list
        List of S&P500 constitutes

    Examples
    --------
    >>> constitutes = sp500_constitutes(fname="sp500.txt")
    >>> constitutes[3]
    >>> 'AAPL'
    """
    with open(fname, 'r') as txt_file:
        _constitutes = txt_file.read()
    return list(filter(None, _constitutes.split('\n')))


def get_prices():
    """Get adjusted close prices for S&P500 constitutes.

    Returns
    -------
    prices: pandas.DataFrame
        Table of tickers and (adjusted) close prices

    Examples
    --------
    >>> from reader import get_prices
    >>> prices = get_prices() # pandas DataFrame
    >>> symbols = prices.columns # list of S&P500 constitutes
    >>> aapl = prices['AAPL'] # Apple price
    """
    prices = pd.read_csv('prices.csv', parse_dates=True, index_col=0)
    return prices


#########################################################################


def _get(symbol, start=None, end=None, source='quandl'):
    """Helper function for `web.DataReader`.

    Parameters
    ----------
    symbol: str
        Ticker symbols (i.e 'AAPL' for Apple)
    start: str | datetime.date
        Start date
    end: str | datetime.date
        End date
    source: str ('quandl', 'yahoo')
        Source of data

    Returns
    -------
    price: pandas.Series
        Adjusted close price for ticker
    """
    _close_col = {'quandl': 'Close', 'yahoo': 'Adj Close'}
    try:
        prices = web.DataReader(symbol, source, start, end)[_close_col[source]]
    except:
        warnings.warn('[%s] unable to reach %s' % (source, symbol))
        prices = pd.Series()
    return prices


def _get_pricing(tickers, start=None, end=None, source='quandl'):
    """Get prices for tickers.

    Parameters
    ----------
    tickers: list
        List of `str` ticker symbols (i.e 'AAPL' for Apple)
    start: str | datetime.date
        Start date
    end: str | datetime.date
        End date
    source: str ('quandl', 'yahoo')
        Source of data

    Returns
    -------
    prices: pandas.DataFrame
        Table of tickers and (adjusted) close prices

    Examples
    --------
    >>> df = get_pricing(['AAPL', 'GOOG'],
    start="2016-01-01", end="2017-01-01", source="yahoo")
    >>> type(df)
    >>> pandas.DataFrame
    >>> type(df.AAPL)
    >>> pandas.Series
    """
    return pd.DataFrame.from_dict({symbol: _get(symbol, start, end, source) for symbol in tickers})


def _export_csv():
    """Export data to `prices.csv`."""
    symbols = sp500_constitutes()
    data = _get_pricing(symbols, start="2010-01-01")
    data.to_csv('prices.csv')
