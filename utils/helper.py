import os
import configparser

dirpath = os.path.dirname(os.path.abspath(__file__))
parentpath = os.path.join(dirpath, os.pardir)
filepath = parentpath+'/config/config.ini'

def read_config():
    config = configparser.ConfigParser()
    config.read(filepath)
    return config