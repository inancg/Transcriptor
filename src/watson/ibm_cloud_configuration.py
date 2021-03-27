import json
import os
from src.common.constants import IBM_CLOUD_CONFIG_LOCATION


class IBMCloudConfiguration:
    def __init__(self):
        with open(os.path.join(os.path.dirname(__file__),
                               IBM_CLOUD_CONFIG_LOCATION)) as cfg_json:
            conf = json.load(cfg_json)
        self.apikey = conf["apikey"]
        self.url = conf["url"]
