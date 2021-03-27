from src.aws.response_handler import ResponseHandler as ResponseHandlerAWS
from src.aws.transcribe_handler import TranscribeHandler as TranscribeHandlerAWS
from src.watson.transcribe_handler import TranscribeHandler as TranscribeHandlerIBM
from src.watson.response_handler import ResponseHandler as ResponseHandlerIBM
import os

is_run_aws = False
_RESOURCES_LOCATION = os.path.join(os.path.dirname(__file__), '../resources/')

if __name__ == '__main__':
    if is_run_aws:
        # Create AWS handlers
        response_handler = ResponseHandlerAWS()
        transcribe_handler = TranscribeHandlerAWS(bucket_name="<bucket_name>")

        # Create a job to transcribe file at s3_uri
        json_url = transcribe_handler.transcribe(media_uri="<s3_uri>")
        print(json_url)

        # Fetch the result json from url and create transcript
        print(response_handler.create_transcript(json_url="<json_url>"))

    else:
        #transcribe_handler = TranscribeHandlerIBM()
        #transcription_result = transcribe_handler.transcribe("t-001.wav")
        response_handler = ResponseHandlerIBM()
        print(response_handler.create_transcript(json_file=_RESOURCES_LOCATION+"watson-001.json"))


