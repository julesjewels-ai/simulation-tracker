"""
Core application logic for PulseUX.

Handles the integration logic for Whisper.cpp (ASR) and Ollama (LLM Analysis).
"""

from typing import Literal, Optional
from .analyzer import StimulationAnalyzer
from .transcriber import AudioTranscriber


class PulseUXTracker:
    """
    Main tracker class responsible for analyzing input and calculating
    stimulation metrics.
    """

    def __init__(
        self,
        ollama_host: str = "http://localhost:11434",
        model_path: str = "models/ggml-base.en.bin",
    ) -> None:
        """
        Initialize the tracker.

        Args:
            ollama_host (str): URL for the local Ollama instance.
            model_path (str): Path to the Whisper GGML model.
        """
        try:
            self.analyzer = StimulationAnalyzer(host=ollama_host)
            self.transcriber = AudioTranscriber(model_path=model_path)
        except Exception as e:
            print(f"Failed to initialize PulseUXTracker: {e}")
            raise

    def process_input(
        self, data: str, mode: Literal["text", "voice"] = "text"
    ) -> float:
        """
        Process input data and return a stimulation score (0.0 - 1.0).

        Args:
            data: Text content or file path to audio.
            mode: 'text' or 'voice'.

        Returns:
            float: A score representing stimulation/intensity level, or 0.0 on failure.
        """
        text_content: Optional[str] = data

        if mode == "voice":
            text_content = self._transcribe_audio(data)
            if text_content:
                print(f"[Transcribed]: {text_content}")
            else:
                print("Transcription failed.")
                return 0.0

        if not text_content:
            return 0.0

        score = self._analyze_stimulation(text_content)
        return score if score is not None else 0.0

    def _transcribe_audio(self, file_path: str) -> Optional[str]:
        """
        Transcribes audio using the AudioTranscriber.
        """
        return self.transcriber.transcribe(file_path)

    def _analyze_stimulation(self, text: str) -> Optional[float]:
        """
        Analyzes text using the StimulationAnalyzer.
        """
        return self.analyzer.analyze(text)

    def visualize(self, level: float) -> None:
        """
        Prints a simple CLI visualization of the stimulation level.
        """
        bar_length = 20
        filled_length = int(bar_length * level)
        bar = "█" * filled_length + "-" * (bar_length - filled_length)
        percent = level * 100

        color = "\033[92m"  # Green
        if level > 0.4:
            color = "\033[93m"  # Yellow
        if level > 0.7:
            color = "\033[91m"  # Red
        reset = "\033[0m"

        print(f"Stimulation: {color}[{bar}] {percent:.1f}%{reset}")
