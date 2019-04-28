
import os, sys
import numpy as np
import pandas as pd
import logging
from utils import setup_logger
from data import load_symbol

from typing import Dict

def mavg_cr(params : Dict[str, int],  dataParams : Dict[str, str], logger : logging = None) -> pd.DataFrame:
    """ Moving Average Cross Strategy """
    """ params.S : short period """
    """ params.L : long period """
    """ Long when short mvag cross over the long mvag from below, vice versa. """
    if logger is None:
        logger = setup_logger("mavg_logger")

    data = pd.DataFrame()
    try:
        exch, sym, freq, resample_to = dataParams["exch"], dataParams["sym"], dataParams["freq"], dataParams["resample_to"]
        data = load_symbol(exch, sym, freq, resample_to)
    except KeyError as e:
        logger.error(f"Couldn't load data for strategy mavg with data {dataParams}, {e}.")
    else:
        logger.info("Loaded data for strategy mavg {params}.")

    try:
        S, L, D = params["S"], params["L"], params["D"]
    except KeyError as e:
        logger.error(f"No defined S/L in mavg, {e}.")
    else:
        if "close" in data.columns:
            close = pd.DataFrame({"close" : data["close"]})
            s_avg = close.rolling(window=S, min_periods=int(S/2)).mean()
            l_avg = close.rolling(window=L, min_periods=int(L/2)).mean()
            data["short"] = s_avg["close"]
            data["long"] = l_avg["close"]
            data["signal"] = 0.0
            data.loc[data["short"].shift(D) > data["long"].shift(D), "signal"] = 1.0
            data.loc[data["short"].shift(D) < data["long"].shift(D), "signal"] = -1.0

    return data



if __name__ == "__main__":

    pars = {"S" : 5, "L" : 10, "D" : 0}
    data_pars = {"exch" : "binance", "sym" : "ADAUSDT", "freq" : "1h", "resample_to" : "1h"}
    df = mavg_cr(pars, data_pars)

    print(df.head(20))
