import unittest

from src.common.response_handler import ResponseHandlerBase
from src.common.transcribe_item import TranscribeItem, TranscribeItemType


from tests.common.constants import TEST_CONFIDENCE_THRESHOLD, \
    TEST_CONFIDENCE_SUSPICIOUS, TEST_CONFIDENCE_NOT_SUSPICIOUS


def create_transcribe_item(
        content, confidence, start_time, end_time, item_type):
    return TranscribeItem(content=content, confidence=confidence,
                          start_time=start_time, end_time=end_time,
                          item_type=item_type)


class TestShouldSuspect(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.response_handler = ResponseHandlerBase(confidence_threshold=
                                                   TEST_CONFIDENCE_THRESHOLD)

    def test_suspicious_item_suspected(self):
        suspicious_item = create_transcribe_item(
            content=None, confidence=TEST_CONFIDENCE_SUSPICIOUS,
            start_time=None, end_time=None, item_type=TranscribeItemType.WORD)

        self.assertEqual(
            self.response_handler.should_suspect(suspicious_item), True)

    def test_not_suspicious_item_not_suspected(self):
        non_suspicious_item = create_transcribe_item(
            content=None, confidence=TEST_CONFIDENCE_NOT_SUSPICIOUS,
            start_time=None, end_time=None, item_type=TranscribeItemType.WORD)

        self.assertEqual(
            self.response_handler.should_suspect(non_suspicious_item), False)


if __name__ == '__main__':
    unittest.main()
