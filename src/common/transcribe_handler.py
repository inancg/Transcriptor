from abc import ABC, abstractmethod


class TranscribeHandlerBase(ABC):
    @abstractmethod
    def transcribe(self, file_name) -> str:
        """
        Platform-specific implementation.
        Transcribes an audio file.
        :param file_name: name of the audio file
        :return: job results as a json string: todo or uri?
        :raise: if job fails
        """
