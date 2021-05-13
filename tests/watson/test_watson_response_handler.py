import unittest

from src.watson.response_handler import ResponseHandler \
    as WatsonResponseHandler
from tests.common.constants import WATSON_TEST_RESOURCES_LOCATION, \
    TEST_CONFIDENCE_THRESHOLD, TRANSCRIBE_ITEMS_SUSPICIOUS_WATSON, \
    TRANSCRIBE_ITEMS_NOT_SUSPICIOUS_WATSON, \
    TRANSCRIBE_ITEMS_NOT_SUSPICIOUS_TWO_SENTENCES_WATSON


class TestWatsonResponseHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.response_handler = WatsonResponseHandler(confidence_threshold=
                                                     TEST_CONFIDENCE_THRESHOLD)

    def test_extract_results_with_suspicion(self):
        self.assertListEqual(
            self.response_handler.extract_results(
                json_file=WATSON_TEST_RESOURCES_LOCATION + 'suspicious.json'),
            TRANSCRIBE_ITEMS_SUSPICIOUS_WATSON  # TODO replace
        )

    def test_extract_results_without_suspicion(self):
        a = self.response_handler.extract_results(
            json_file=WATSON_TEST_RESOURCES_LOCATION + 'not_suspicious'
                                                       '.json')
        self.assertListEqual(
            self.response_handler.extract_results(
                json_file=WATSON_TEST_RESOURCES_LOCATION + 'not_suspicious'
                                                           '.json'),
            TRANSCRIBE_ITEMS_NOT_SUSPICIOUS_WATSON
        )

    def test_extract_results_without_suspicion_two_sentences(self):
        self.assertListEqual(
            self.response_handler.extract_results(
                json_file=WATSON_TEST_RESOURCES_LOCATION +
                          'not_suspicious_two_sentences.json'),
            TRANSCRIBE_ITEMS_NOT_SUSPICIOUS_TWO_SENTENCES_WATSON
        )


if __name__ == '__main__':
    unittest.main()
