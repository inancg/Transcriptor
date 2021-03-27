from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from src.watson.ibm_cloud_configuration import IBMCloudConfiguration
from src.common.transcribe_handler import TranscribeHandlerBase
from src.common.constants import RESOURCES_LOCATION, WATSON_MAX_ALTERNATIVES,\
    WATSON_WORD_ALTERNATIVES_THRESHOLD, WATSON_SPLIT_AT_PHRASE_END,\
    WATSON_JOB_FINISHED_STATUS

import os
import time


class TranscribeHandler(TranscribeHandlerBase):
    def __init__(self):
        # Read from configuration file
        self.conf = IBMCloudConfiguration()
        self.authenticator = IAMAuthenticator(apikey=self.conf.apikey)
        # Define speech to text handler
        self.stt = SpeechToTextV1(authenticator=self.authenticator)
        self.stt.service_url = self.conf.url

    def transcribe(self, file_name):
        file_path = os.path.join(RESOURCES_LOCATION, file_name)
        file_extension = file_name.split(".")[-1]
        content_type = 'audio/{}'.format(file_extension)

        job = self.create_job(file_path, content_type)
        job_id = job["id"]
        job_result = self.get_job_result(job_id)  # blocking

        return job_result

    def create_job(self, file_path, content_type):
        with open(file_path, 'rb') as audio_file:
            recognition_job = self.stt.create_job(
                audio_source=AudioSource(audio_file),
                audio=audio_file,
                model='en-US_BroadbandModel',
                content_type=content_type,
                max_alternatives=WATSON_MAX_ALTERNATIVES,
                word_alternatives_threshold=WATSON_WORD_ALTERNATIVES_THRESHOLD,
                split_transcript_at_phrase_end=WATSON_SPLIT_AT_PHRASE_END
            ).get_result()
        return recognition_job

    def get_job_result(self, job_id):
        while True:
            job = self.check_job(job_id)
            if job["status"] in WATSON_JOB_FINISHED_STATUS:
                break
            print("{} {}".format(job["status"], job["updated"]))
            time.sleep(10)  # TODO implement in a better way

        return job["results"]

    def check_job(self, job_id):
        return self.stt.check_job(job_id).get_result()
