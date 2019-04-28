
import os, sys
import numpy as np
import pandas as pd
import logging

from utils import setup_logger


def load_symbol(exch : str, sym : str, freq : str, resample_to : str, data_dir : str = "all_coins", logger : logging = None) -> pd.DataFrame:
    if logger is None:
        logger = setup_logger("data_logger")

    path = os.path.expandvars(data_dir)
    filename = os.path.join(path, f"{exch}_{sym}_{freq}.csv")

    df = pd.DataFrame()

    try:
        df = pd.read_csv(filename, index_col=[0], parse_dates=[0])
    except IOError as e:
        logger.error(f"Couldn't load file {filename}")

    if not df.empty and freq != resample_to:
        try:
            op = df["open"].resample(resample_to, label="left", closed="left").first()
            hi = df["high"].resample(resample_to, label="left", closed="left").max()
            lo = df["low"].resample(resample_to, label="left", closed="left").min()
            cl = df["close"].resample(resample_to, label="left", closed="left").last()
            vo = df["volume"].resample(resample_to, label="left", closed="left").sum()
            df = pd.DataFrame({"open":op, "high":hi, "low":lo, "close":cl, "volume":vo})
        except Exception as e:
            logger.error(f"Couldn't resample {filename} from {freq} to {resample_to}.")

    return df


if __name__ == "__main__":

    df = load_symbol("binance", "ADAUSDT", "1h", "1h")
    print(df)
