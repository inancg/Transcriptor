import boto3
import time
import uuid
import os

from src.common.transcribe_handler import TranscribeHandlerBase
from src.common.constants import AWS_JOB_FINISHED_STATUS,\
    AWS_STATUS_COMPLETED, AWS_TRANSCRIBE, AWS_S3


class TranscribeHandler(TranscribeHandlerBase):
    def __init__(self, bucket_name=None):  # TODO fix Nones
        self.bucket_name = bucket_name

    def transcribe(self, media_uri) -> str:
        # Create transcribe client
        transcribe_client = boto3.client(AWS_TRANSCRIBE)
        # Create random job name
        job_name = str(uuid.uuid4())

        # Returns result json url
        transcribe_client.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={'MediaFileUri': media_uri},
            MediaFormat='wav',
            LanguageCode='en-US',
            Settings={
                'MaxAlternatives': 3,
                'ShowAlternatives': True
            }
        )

        counter = 0  # TODO remove this counter logic, very wrong
        while counter < 50:
            result = transcribe_client\
                .get_transcription_job(TranscriptionJobName=job_name)
            job_status = result['TranscriptionJob']['TranscriptionJobStatus']
            if job_status in AWS_JOB_FINISHED_STATUS:
                break
            print("Sleeping")
            counter += 5  # TODO remove this counter logic, very wrong
            time.sleep(5)  # TODO magic number but ok

        if job_status == AWS_STATUS_COMPLETED:
            return result['TranscriptionJob']['Transcript']['TranscriptFileUri']

        # TODO return json string instead of uri?

        raise Exception("Job takes too long")  # TODO better exception?

    def upload_to_database(self, file_name):
        # Create s3 client
        s3_client = boto3.client(AWS_S3)

        object_name = os.path.basename(file_name)
        with open(file_name, "rb") as f:
            s3_client.upload_fileobj(f, self.bucket_name, object_name)

    def create_bucket(self, bucket_prefix):
        # Create s3 resource
        s3_resource = boto3.resource(AWS_S3)

        session = boto3.session.Session()
        current_region = session.region_name
        bucket_name = self.create_bucket_name(bucket_prefix)
        bucket_response = s3_resource.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': current_region})
        print(bucket_name, current_region)
        return bucket_name, bucket_response

    @staticmethod
    def create_bucket_name(bucket_prefix):
        return ''.join([bucket_prefix, str(uuid.uuid4())])
