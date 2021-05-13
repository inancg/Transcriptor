from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize


class SentenceAnalyser:
    @staticmethod
    def does_start_with_cc(phrase: str):
        part_of_speech = pos_tag(word_tokenize(phrase))
        return len(part_of_speech) > 0 and part_of_speech[0][1] == 'CC'

    @staticmethod
    def does_end_with_cc(phrase: str):
        part_of_speech = pos_tag(word_tokenize(phrase))
        return len(part_of_speech) > 0 and part_of_speech[-1][1] == 'CC'
