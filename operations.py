
import os, sys
import numpy as np
import pandas as pd

def mavg_op(signal : pd.DataFrame, field : str = "signal", N : int) -> pd.DataFrame:
    """ Moving average operations on signals """
    try:
        sig = signal[[field]]
        mavg = sig.rolling(window=N, min_periods=1).mean()
        signal["signal"] = mavg["signal"]
    except KeyError as e:
        print(f"Couldn't find signal!")

    return signal

    


