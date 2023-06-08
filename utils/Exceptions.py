import logging
import sys
import os

dirpath = os.path.dirname(os.path.abspath(__file__))

def logger(name):
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    localPath = os.path.join(dirpath,os.pardir+"/logs/")
    if not os.path.exists(localPath):
        os.makedirs(localPath, 0o755)
    
    handler = logging.FileHandler(localPath+name+'.log', mode='a')
    handler.setFormatter(formatter)
    screen_handler = logging.StreamHandler(stream=sys.stdout)
    screen_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    return logger
