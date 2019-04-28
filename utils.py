import os, sys
import logging, logging.handlers

def setup_logger(name : str = "Logger", level : logging = logging.INFO) -> logging:
    print(f"Creating logger {name} with level {level} ...")
    logger = logging.getLogger(name)
    logger.setLevel(level)
    FORMAT = "%(asctime)s %(levelname)s %(message)s"
    logging.basicConfig(format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S")
    return logger

