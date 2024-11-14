"""
Template for submissions to the market-making game

"""

import numpy as np


def make_market(p, d, v, x):

        b0 = 0.2
        b1 = 0.8
        halfspread = 0.03
        x_cutoff = 3
        large_pos_bias = 0.02
        price = b0*p[0] + b1*p[1]
        dividend = b0*d[0] + b1*d[1]
        buy = price - halfspread
        sell = price + halfspread
        if x > 0:
            sell *= (1-large_pos_bias)**x
        if x < 0:
            buy *= (1+large_pos_bias)**abs(x)
        if x <= -x_cutoff:
            sell = 100000
        if x >= x_cutoff:
            buy = 0.000001

        return np.array([buy, sell])
