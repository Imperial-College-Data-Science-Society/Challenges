import pandas as pd
import pandas_datareader.data as web


def get_ivx():
    """Get S&P500 volatility index ^IVX.

    Returns
    -------
    ivx: pandas.Series
        S&P500 volatility index time-series

    Examples
    --------
    >>> ivx = get_ivx()
    >>> type(ivx)
    >>> pandas.Series
    """
    volatility = pd.read_csv('volatility.csv', parse_dates=True, index_col=0)
    return volatility

#########################################################################


def _get_ivx(start=None, end=None):
    """Get S&P500 volatility index ^IVX.

    Parameters
    ----------
    start: str | datetime.date
        Start date
    end: str | datetime.date
        End date

    Returns
    -------
    ivx: pandas.Series
        S&P500 volatility index time-series

    Examples
    --------
    >>> ivx = get_ivx(start="2016-01-01", end="2017-01-01")
    >>> type(ivx)
    >>> pandas.Series
    """
    if end:
        if not start:
            raise ValueError('specify "start" when specifying "end" date.')
    return web.DataReader('^VIX', 'yahoo', start, end)['Adj Close']


def _export_csv():
    """Export data to `volatility.csv`."""
    data = _get_ivx()
    data.to_csv('volatility.csv')
