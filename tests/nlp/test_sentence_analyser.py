import unittest
from src.nlp.sentence_analyser import SentenceAnalyser


class MyTestCase(unittest.TestCase):
    def test_starts_with_CC(self):
        self.assertTrue(SentenceAnalyser.does_start_with_cc(
            "and this test is complete"))
        self.assertFalse(SentenceAnalyser.does_start_with_cc(
            "this test is complete"))

    def test_ends_with_CC(self):
        self.assertTrue(SentenceAnalyser.does_end_with_cc(
            "this test is complete and"))
        self.assertFalse(SentenceAnalyser.does_end_with_cc(
            "this test is complete"))


if __name__ == '__main__':
    unittest.main()
