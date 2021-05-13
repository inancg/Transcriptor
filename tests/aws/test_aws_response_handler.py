import unittest

from src.aws.response_handler import ResponseHandler as AWSResponseHandler
from tests.common.constants import AWS_TEST_RESOURCES_LOCATION, \
    TEST_CONFIDENCE_THRESHOLD, TRANSCRIBE_ITEMS_SUSPICIOUS_AWS, \
    TRANSCRIBE_ITEMS_NOT_SUSPICIOUS_AWS


class TestAWSResponseHandler(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.response_handler = AWSResponseHandler(confidence_threshold=
                                                  TEST_CONFIDENCE_THRESHOLD)

    def test_extract_results_with_suspicion(self):
        self.assertListEqual(
            self.response_handler.extract_results(
                json_file=AWS_TEST_RESOURCES_LOCATION + 'suspicious.json'),
            TRANSCRIBE_ITEMS_SUSPICIOUS_AWS
        )

    def test_extract_results_without_suspicion(self):
        self.assertListEqual(
            self.response_handler.extract_results(
                json_file=AWS_TEST_RESOURCES_LOCATION + 'not_suspicious.json'),
            TRANSCRIBE_ITEMS_NOT_SUSPICIOUS_AWS
        )


if __name__ == '__main__':
    unittest.main()
