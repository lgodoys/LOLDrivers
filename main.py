#!/usr/bin/env python3

#Import common libraries
import json
import requests
import urllib3

#Import external libraries

#Import custom classes and functions
from utils.Exceptions import *
from utils.helper import *

#Set Disable Warnings for HTTPS URL's
urllib3.disable_warnings()

#Set Logger
LOGGER = logger("LOL Drivers")

#Get configurations from config file
LOGGER.info("[ LOLDrivers ] Getting configurations...")
config = read_config()

URL = config['default']['url']
SPLUNK_URL = config['default']['splunk_url']
HEC_TOKEN = config['default']['hec_token']
MAIN_KEYS = list(config['default']['main_keys'].split(','))
SUB_KEY = config['default']['sub_key']
LOGGER.info("[ LOLDrivers ] Configurations obtained from config file.")

#Set Authorization Header for Splunk
LOGGER.info("[ LOLDrivers ] Setting Headers for Splunk push")
headers = {
    "Authorization": f"Splunk {HEC_TOKEN}"
}

#Base logic
try:
    LOGGER.info(f"[ LOLDrivers ] Getting JSON from {URL}")
    resp = requests.get(URL)
    LOGGER.info(f"[ LOLDrivers ] Status code was: {resp.status_code}")
    if resp.status_code == 200:
        LOGGER.info("[ LOLDrivers ] Processing JSON")
        returnJson = resp.json()
        for i in returnJson:
            LOGGER.info(f"[ LOLDrivers ] Filtering by Category")
            if i['Category'] == 'vulnerable driver':
                keys = i.keys()
                for main in MAIN_KEYS:
                    if main in keys:
                        LOGGER.info(f"[ LOLDrivers ] Removing {main} key")
                        del i[main]
                for k in range(len(i["KnownVulnerableSamples"])):
                    if SUB_KEY in i["KnownVulnerableSamples"][k]:
                        LOGGER.info(f"[ LOLDrivers ] Removing {SUB_KEY} from KnownVulnerableSamples")
                        del i["KnownVulnerableSamples"][k][SUB_KEY]
                LOGGER.info("[ LOLDrivers ] Dumping data to JSON format")
                data = json.dumps({'host': 'LOLDrivers.io', 'sourcetype':'loldrivers', 'source':'LOLDrivers','event': i})
                LOGGER.info(f"[ LOLDrivers ] Sending data to {SPLUNK_URL} Splunk Endpoint")
                response = requests.post(url=SPLUNK_URL, headers=headers, data=data, verify=False)
                LOGGER.info(f"[ LOLDrivers ] Splunk Status code was: {response.status_code}")
                if response.status_code != 200:
                    raise response.raise_for_status()
except Exception as err:
    LOGGER.fatal(f"An error was raised: {err}")