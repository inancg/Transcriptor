import json
import pandas as pd
from src.common.response_handler import ResponseHandlerBase
from src.common.transcribe_item import TranscribeItem, TranscribeItemType
from src.common.constants import CC_LIST


class ResponseHandler(ResponseHandlerBase):
    def extract_results(self, json_file=None, json_url=None):
        if json_file:
            with open(json_file, "r") as read_file:
                data = json.load(read_file)
        elif json_url:
            data = json.loads(pd.read_json(json_url).to_json())
        else:
            raise Exception("JSON failed to load")

        return self.clean_results(data['results'][0]['results'])

    def clean_results(self, results: list):
        """
        Watson-specific parse function.
        :param results: includes list of phrases as dictionaries
        :return: list of TranscribeItem
        """
        transcribed_words = []

        for phrase in results:
            transcribed_from_phrase = self.transform_phrase(phrase)
            transcribed_words += self.update_sentence_endings(
                transcribed_from_phrase, transcribed_words)
        return transcribed_words

    def transform_phrase(self, phrase: dict) -> list:
        """
        Transforms a phrase to list of TranscribeItems
        :param phrase: dictionary contains word alternatives
        :return: a list of TranscribeItems
        """
        transcribed_words = [self.transform_to_transcribe_item(word)
                             for word in phrase["word_alternatives"]]

        if phrase["end_of_utterance"] == "full_stop":
            last_item_end_time: float = transcribed_words[-1].end_time

            transcribed_words.append(
                TranscribeItem(content=".",
                               confidence=1.0,
                               start_time=last_item_end_time,
                               end_time=last_item_end_time,
                               item_type=TranscribeItemType.PUNCTUATION))

        return transcribed_words

    def transform_to_transcribe_item(self, item: dict):
        # Will get only the item with the highest confidence.
        return TranscribeItem(content=item["alternatives"][0]["word"],
                              confidence=float(item["alternatives"][0]
                                               ["confidence"]),
                              start_time=item["start_time"],
                              end_time=item["end_time"],
                              item_type=TranscribeItemType.WORD)

    @staticmethod
    def update_sentence_endings(phrase_transcriptions: list,
                                transcribed_words: list):
        """
        Naive low-accuracy sentence detection
        :param transcribed_words: already transcribed words
        :param phrase_transcriptions: comes from phrase, list of TranscribeItem
        :return: updated phrase_transcriptions list
        """
        result = phrase_transcriptions
        if len(transcribed_words) > 0:
            last_transcribed_word = transcribed_words[-1]

            if last_transcribed_word.item_type != \
                    TranscribeItemType.PUNCTUATION and \
                    last_transcribed_word.content.lower() not in CC_LIST and \
                    phrase_transcriptions[0].content.lower() not in CC_LIST:
                last_item_end_time = last_transcribed_word.end_time
                dot = TranscribeItem(
                    content=".",
                    confidence=1.0,
                    start_time=last_item_end_time,
                    end_time=last_item_end_time,
                    item_type=TranscribeItemType.PUNCTUATION)
                result = [dot] + result

        return result
