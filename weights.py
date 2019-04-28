
import os, sys
import numpy as np
import pandas as pd

def ts_equal_weight(signal : pd.DataFrame, field : str = "signal") -> pd.DataFrame:
    """ Equal weight on time series """
    try:
        sig = signal[[field]]
        signal[field] = sig * 1.0
    except KeyError as e:
        print(f"Couldn't find signal!")

    return signal

    


