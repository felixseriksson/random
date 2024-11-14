# BACKTEST
# Do not modify this file. It is used to verify
# your solution before submission.
# (c) GSA Capital 2021


import numpy as np
import pandas as pd
import logging
from solution import make_market

log = logging.getLogger(__name__)
EPS = 1e-5


def _get_trade(price, buy, sell):

    if price < buy:
        trade = 1
    elif price > sell:
        trade = -1
    else:
        trade = 0
    return trade


def _run(f, data):

    inv_pnl = pd.Series(index=data.t, data=0)
    div_pnl = pd.Series(index=data.t, data=0)
    fin_pnl = pd.Series(index=data.t, data=0)
    positions = pd.Series(index=data.t, data=0)

    b = EPS
    s = np.inf
    old = 0
    new = 0

    rows = list(data.itertuples(index=False))
    previous = rows[:-1]
    current = rows[1:]

    for rp, r in zip(previous, current):

        # This loop is taking place immediately after the auction at
        # time t.

        # Compute pnl from rp.t to r.t
        t = r.t
        inv_pnl.loc[t] = (r.P - rp.P) * old
        div_pnl.loc[t] = r.D * old
        fin_pnl.loc[t] = -0.01 * (old * rp.P) - 0.001 * (old * rp.P) ** 2

        # update position
        trade = _get_trade(r.P, b, s)
        new = old + trade
        positions.loc[t] = new
        old = new

        # calculate buy and sell price for the next auction
        p = np.array([rp.P, r.P])
        d = np.array([rp.D, r.D])
        v = np.array([rp.V, r.V])
        b, s = f(p, d, v, new)

    results = pd.DataFrame({
        'position': positions,
        'inventory pnl': inv_pnl,
        'dividend pnl': div_pnl,
        'financing pnl': fin_pnl,
        'total pnl': inv_pnl + div_pnl + fin_pnl,
    })

    return results


def run(key='train', plot=True):
    """
    Run a backtest.

    Args:
        key (str): data set to use for evaluation. Either 'train' or 'test'
        plot (bool): if True, will plot cumulative pnl over time

    Returns:
        frame: dataframe giving position and components of pnl over time

    """

    df = pd.read_csv(f'{key}.csv')
    results = _run(make_market, df)

    if plot:
        import matplotlib.pyplot as plt
        plt.ion()
        results.drop('position', axis=1).cumsum().plot()

    return results

def my_run(fn_to_backtest, key='train', plot=True):
    """
    Run a backtest.

    Args:
        key (str): data set to use for evaluation. Either 'train' or 'test'
        plot (bool): if True, will plot cumulative pnl over time

    Returns:
        frame: dataframe giving position and components of pnl over time

    """

    df = pd.read_csv(f'{key}.csv')
    results = _run(fn_to_backtest, df)

    if plot:
        import matplotlib.pyplot as plt
        plt.ion()
        results.drop('position', axis=1).cumsum().plot()

    return results