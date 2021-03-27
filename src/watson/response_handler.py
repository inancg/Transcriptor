import json
import pandas as pd
from src.common.response_handler import ResponseHandlerBase


class ResponseHandler(ResponseHandlerBase):
    def extract_results(self, json_file=None, json_url=None):
        # TODO implement
        if json_file:
            with open(json_file, "r") as read_file:
                data = json.load(read_file)
        elif json_url:
            data = json.loads(pd.read_json(json_url).to_json())
        else:
            raise Exception("JSON failed to load")

        return self.clean_results(data['results'])

    def clean_results(self, results):
        """
        TODO implement> Watson-specific parse function.
        :param results: a part of raw json response from Watson
        :return: list of TranscribeItem
        """
        raise NotImplementedError