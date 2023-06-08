# LOLDrivers

LOLDrivers is a Python application that allows to Splunk manager to push data from LOLDrivers endpoint to Splunk using Splunk HTTP Event Collector. For usage, requires a Splunk environment with HEC enabled.

## Installation

Download this package from GitHub or clone this repository to your destination folder using git clone command.

## Configuration

Set config.ini file in config folder with following parameters (use config.ini.example as base, but, create a config.ini file inside the folder):

```ini
[default]
hec_token = Your Splunk HTTP Event Collector token
splunk_url = https://{Splunk_server}:8088/services/collector/event
url = https://www.loldrivers.io/api/drivers.json
main_keys = Your main keys to remove
sub_key = Single subkeys to remove (if required, needs to process new logic. Useful with only one subkey for now)
```

The config file will allows the app to connect to LOLDrivers API endpoint, and allows the app to send data to Splunk endpoint. The "main_keys" and "sub_key" config keys are used to remove specific keys and subkeys from JSON. In development yet.

Configure your own cronjob using main.py. This file must be executable in Unix environment. Be sure that the main file has +x permissions.

## Recommended environment

The app was developed on a Linux environment. It is fully recommended to use a Linux environment, for compatibility.

In case you need to use a Windows environment, please, open an issue and will be processed in a new iteration.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropiate.

## License

[MIT](https://choosealicense.com/licenses/mit)
