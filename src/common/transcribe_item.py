from enum import Enum


class TranscribeItem:
    def __init__(self, content, confidence, start_time, end_time, item_type):
        self.content = content
        self.confidence = confidence
        self.start_time = start_time
        self.end_time = end_time
        self.item_type = item_type

    def __eq__(self, other):
        return self.content == other.content and \
               self.confidence == other.confidence and \
               self.start_time == other.start_time and \
               self.end_time == other.end_time and \
               self.item_type == other.item_type

    def __repr__(self):
        return "{} [{}]".format(self.content, self.confidence)


class TranscribeItemType(Enum):
    PUNCTUATION = 1
    WORD = 2
