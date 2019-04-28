
import os, sys
import numpy as np
import pandas as pd
import logging
from utils import setup_logger
from data import load_symbol

from typing import Dict
from signals import mavg_cr

from typing import Callable

from operations import *
from weights import *


class stats(object):
    def __init__(self, 
                 data : pd.DataFrame, 
                 signal : str = "signal", 
                 operation callable: 
                 weight : callable, 
                 logger : logging = None) -> None:
        if logger is None:
            logger = setup_logger("stats_logger")
        self.data = data
        operation(self.data)
        weight(self.data)
        self.data["position"] = self.data["signal"].shift(1)
        ret = np.log(self.data["close"]).diff()
        self.data["PnL"] = self["position"].shift(1).mul(ret)
