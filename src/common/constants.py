import os
RESOURCES_LOCATION = os.path.join(os.path.dirname(__file__),
                                  '../../resources/')
CONFIDENCE_THRESHOLD: float = 0.8

# IBM Cloud Constant
IBM_CLOUD_CONFIG_LOCATION = os.path.join(RESOURCES_LOCATION, 'ibm_cloud.json')

# AWS Constants
AWS_STATUS_COMPLETED = 'COMPLETED'
AWS_STATUS_FAILED = 'FAILED'
AWS_JOB_FINISHED_STATUS = [AWS_STATUS_COMPLETED, AWS_STATUS_FAILED]
AWS_TRANSCRIBE = 'transcribe'
AWS_S3 = 's3'

# IBM Watson Constants
WATSON_STATUS_COMPLETED = 'completed'
WATSON_STATUS_FAILED = 'failed'
WATSON_JOB_FINISHED_STATUS = [WATSON_STATUS_COMPLETED, WATSON_STATUS_FAILED]
WATSON_MAX_ALTERNATIVES = 3
WATSON_WORD_ALTERNATIVES_THRESHOLD = 0.1
WATSON_SPLIT_AT_PHRASE_END = True

# Sentence Analysis
CC_LIST = ["and", "but", "or", "nor", "if", "whether"]
