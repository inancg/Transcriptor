import json
import pandas as pd
from src.common.response_handler import ResponseHandlerBase
from src.common.transcribe_item import TranscribeItem, TranscribeItemType


class ResponseHandler(ResponseHandlerBase):
    last_item_end_time = 0

    def extract_results(self, json_file=None, json_url=None):
        if json_file:
            with open(json_file, "r") as read_file:
                data = json.load(read_file)
        elif json_url:
            data = json.loads(pd.read_json(json_url).to_json())
        else:
            raise Exception("JSON failed to load")

        return [self.transform_to_transcribe_item(item)
                for item in data['results']['items']]

    def transform_to_transcribe_item(self, item) -> TranscribeItem:
        if item['type'] == "pronunciation":
            self.last_item_end_time = item['end_time']
            return TranscribeItem(content=item['alternatives'][0]['content'],
                                  confidence=float(item['alternatives'][0] \
                                      ['confidence']),
                                  start_time=float(item['start_time']),
                                  end_time=float(item['end_time']),
                                  item_type=TranscribeItemType.WORD)
        elif item['type'] == "punctuation":
            return TranscribeItem(content=item['alternatives'][0]['content'],
                                  confidence=1.0,
                                  start_time=float(self.last_item_end_time),
                                  end_time=float(self.last_item_end_time),
                                  item_type=TranscribeItemType.PUNCTUATION)
        else:
            raise Exception("Invalid item : {}".format(item))
