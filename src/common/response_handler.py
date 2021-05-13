from src.common.transcribe_item import TranscribeItem
from src.common.constants import CONFIDENCE_THRESHOLD


class ResponseHandlerBase:
    def __init__(self, confidence_threshold=CONFIDENCE_THRESHOLD):
        self._CONFIDENCE_THRESHOLD = confidence_threshold
        self.suspicion_zones = []
        print("Created handler with confidence threshold : ",
              self._CONFIDENCE_THRESHOLD)

    def create_transcript(self, json_file=None, json_url=None):
        """
        Main method. Creates transcript from input json
        :param json_file: path to a local json file
        :param json_url: url to a json file
        :return:
        """
        # Read json into results dict
        results = self.extract_results(json_file=json_file, json_url=json_url)
        result_transcript = ""

        item: TranscribeItem
        for item in results:
            if self.should_suspect(item):
                item_start_time = item.start_time
                result_transcript += "**<{}>** ".format(item_start_time)
            else:
                result_transcript += item.content + " "
        return result_transcript

    def extract_results(self, json_file=None, json_url=None):
        """
        :param json_file: path to a local json file
        :param json_url: url to a json file
        :return: list of TranscribeItem
        """
        raise NotImplementedError

    def transform_to_transcribe_item(self, item: dict) -> TranscribeItem:
        """
        Helper function for extract results.
        :param item: domain-specific dictionary
        :return: the input as a TranscribeItem
        """
        raise NotImplementedError

    def should_suspect(self, item: TranscribeItem):
        """
        Checks if the confidence of the item is lower than the threshold
        :param item:
        :return:
        """
        return float(item.confidence) < self._CONFIDENCE_THRESHOLD
