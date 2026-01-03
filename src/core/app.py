"""
Core application logic for PulseUX.

Handles the integration logic for what would eventually be 
Whisper.cpp (ASR) and Ollama (LLM Analysis).
"""

import random
import time
from typing import Literal

class PulseUXTracker:
    """
    Main tracker class responsible for analyzing input and calculating
    stimulation metrics.
    """

    def __init__(self, ollama_host: str = "http://localhost:11434") -> None:
        """
        Initialize the tracker.
        
        Args:
            ollama_host: URL for the local Ollama instance (placeholder for future use).
        """
        self.ollama_host = ollama_host
        # In a real MVP, we would initialize Whisper context here

    def process_input(self, data: str, mode: Literal["text", "voice"] = "text") -> float:
        """
        Process input data and return a stimulation score (0.0 - 1.0).

        Args:
            data: Text content or file path to audio.
            mode: 'text' or 'voice'.

        Returns:
            float: A score representing stimulation/intensity level.
        """
        text_content = data

        if mode == "voice":
            text_content = self._transcribe_audio(data)
            print(f"[Transcribed]: {text_content}")

        return self._analyze_stimulation(text_content)

    def _transcribe_audio(self, file_path: str) -> str:
        """
        Mock wrapper for Whisper.cpp.
        In a real scenario, this would call bindings for whisper.cpp.
        """
        # Simulating processing delay
        time.sleep(0.5)
        return f"(Simulated transcription of {file_path}) This is exciting!"

    def _analyze_stimulation(self, text: str) -> float:
        """
        Mock wrapper for Ollama sentiment/stimulation analysis.
        Returns a float between 0.0 and 1.0.
        """
        # Simple heuristic for MVP demonstration purposes
        # Real implementation would prompt an LLM via API
        base_score = 0.2
        
        # Arbitrary rules to simulate AI detection
        if "!" in text: 
            base_score += 0.3
        if len(text) > 20:
            base_score += 0.2
        if "exciting" in text.lower() or "wow" in text.lower():
            base_score += 0.3
            
        return min(base_score, 1.0)

    def visualize(self, level: float) -> None:
        """
        Prints a simple CLI visualization of the stimulation level.
        """
        bar_length = 20
        filled_length = int(bar_length * level)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        percent = level * 100
        
        color = "\033[92m" # Green
        if level > 0.4: color = "\033[93m" # Yellow
        if level > 0.7: color = "\033[91m" # Red
        reset = "\033[0m"
        
        print(f"Stimulation: {color}[{bar}] {percent:.1f}%{reset}")
