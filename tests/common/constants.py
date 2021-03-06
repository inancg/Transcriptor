import os
from src.common.transcribe_item import TranscribeItem, TranscribeItemType

TEST_RESOURCES_LOCATION = os.path.join(os.path.dirname(__file__),
                                       '../resources/')

AWS_TEST_RESOURCES_LOCATION = TEST_RESOURCES_LOCATION + 'aws/'
WATSON_TEST_RESOURCES_LOCATION = TEST_RESOURCES_LOCATION + 'watson/'

TEST_CONFIDENCE_THRESHOLD: float = 0.8
TEST_CONFIDENCE_SUSPICIOUS: float = 0.4
TEST_CONFIDENCE_NOT_SUSPICIOUS: float = 0.95

TRANSCRIBE_ITEMS_SUSPICIOUS_AWS = [
        TranscribeItem(content="This", confidence=1, start_time=1,
                       end_time=1.5, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="is", confidence=0.9, start_time=1.5,
                       end_time=2, item_type=TranscribeItemType.WORD),
        TranscribeItem(content=",", confidence=1, start_time=2,
                       end_time=2, item_type=TranscribeItemType.PUNCTUATION),
        TranscribeItem(content="probably", confidence=0.4, start_time=2.5,
                       end_time=3, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="a", confidence=0.8, start_time=3,
                       end_time=3.2, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="test", confidence=0.6, start_time=3.5,
                       end_time=4, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="case", confidence=0.96, start_time=4,
                       end_time=4.5, item_type=TranscribeItemType.WORD),
        TranscribeItem(content=".", confidence=1, start_time=4.5,
                       end_time=4.5, item_type=TranscribeItemType.PUNCTUATION),
        TranscribeItem(content="Should", confidence=0.2, start_time=6,
                       end_time=6.5, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="it", confidence=0.85, start_time=6.5,
                       end_time=7, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="pass", confidence=0.95, start_time=7,
                       end_time=7.5, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="?", confidence=1, start_time=7.5,
                       end_time=7.5, item_type=TranscribeItemType.PUNCTUATION)
        ]

TRANSCRIBE_ITEMS_NOT_SUSPICIOUS_AWS = [
        TranscribeItem(content="This", confidence=1, start_time=1,
                       end_time=1.5, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="is", confidence=0.9, start_time=1.5,
                       end_time=2, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="it", confidence=1, start_time=2.1,
                       end_time=2.3, item_type=TranscribeItemType.WORD),
        TranscribeItem(content=".", confidence=1, start_time=2.3,
                       end_time=2.3, item_type=TranscribeItemType.PUNCTUATION)
        ]

TRANSCRIBE_ITEMS_NOT_SUSPICIOUS_WATSON = [
        TranscribeItem(content="this", confidence=1, start_time=0,
                       end_time=0.1, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="is", confidence=0.99, start_time=0.1,
                       end_time=0.2, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="a", confidence=0.9, start_time=0.2,
                       end_time=0.3, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="test", confidence=0.91, start_time=0.3,
                       end_time=0.4, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="and", confidence=0.92, start_time=0.4,
                       end_time=0.5, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="nothing", confidence=0.96, start_time=0.5,
                       end_time=0.6, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="suspicious", confidence=0.93, start_time=0.6,
                       end_time=0.7, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="is", confidence=0.93, start_time=0.7,
                       end_time=0.8, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="happening", confidence=0.96, start_time=0.9,
                       end_time=1.0, item_type=TranscribeItemType.WORD),
        TranscribeItem(content=".", confidence=1, start_time=1.0,
                       end_time=1.0, item_type=TranscribeItemType.PUNCTUATION)
        ]

TRANSCRIBE_ITEMS_NOT_SUSPICIOUS_TWO_SENTENCES_WATSON = [
        TranscribeItem(content="this", confidence=1, start_time=0,
                       end_time=0.1, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="is", confidence=0.99, start_time=0.1,
                       end_time=0.2, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="a", confidence=0.9, start_time=0.2,
                       end_time=0.3, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="test", confidence=0.91, start_time=0.3,
                       end_time=0.4, item_type=TranscribeItemType.WORD),
        TranscribeItem(content=".", confidence=1, start_time=0.4,
                       end_time=0.4, item_type=TranscribeItemType.PUNCTUATION),
        TranscribeItem(content="absolutely", confidence=0.92, start_time=0.4,
                       end_time=0.5, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="nothing", confidence=0.96, start_time=0.5,
                       end_time=0.6, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="suspicious", confidence=0.93, start_time=0.6,
                       end_time=0.7, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="is", confidence=0.93, start_time=0.7,
                       end_time=0.8, item_type=TranscribeItemType.WORD),
        TranscribeItem(content="happening", confidence=0.96, start_time=0.9,
                       end_time=1.0, item_type=TranscribeItemType.WORD),
        TranscribeItem(content=".", confidence=1, start_time=1.0,
                       end_time=1.0, item_type=TranscribeItemType.PUNCTUATION)
        ]

TRANSCRIBE_ITEMS_SUSPICIOUS_WATSON = []  # TODO fill
