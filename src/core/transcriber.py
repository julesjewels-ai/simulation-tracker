"""
Audio transcription using Whisper.cpp.
"""

from typing import Optional
from whisper_cpp_python import Whisper


class AudioTranscriber:
    """
    Transcribes audio files to text using Whisper.cpp.
    """

    def __init__(self, model_path: str = "models/ggml-base.en.bin"):
        """
        Initialize the transcriber with a Whisper model.

        Args:
            model_path (str): The path to the GGML model file.
        """
        try:
            self.model = Whisper(model_path=model_path)
        except Exception as e:
            print(f"Error loading Whisper model from '{model_path}': {e}")
            print("Please ensure the model file exists and is accessible.")
            raise

    def transcribe(self, file_path: str) -> Optional[str]:
        """
        Transcribes an audio file and returns the text.

        Args:
            file_path (str): The path to the audio file.

        Returns:
            Optional[str]: The transcribed text, or None if transcription fails.
        """
        try:
            result = self.model.transcribe(file_path)
            return result["text"].strip()

        except Exception as e:
            print(f"An error occurred during transcription: {e}")
            return None
