from enum import Enum


class TranscribeItem:
    def __init__(self, content, confidence, start_time, end_time, item_type):
        self.content = content
        self.confidence = confidence
        self.start_time = start_time
        self.end_time = end_time
        self.item_type = item_type


class TranscribeItemType(Enum):
    PUNCTUATION = 1
    WORD = 2
