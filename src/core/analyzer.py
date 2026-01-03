"""
Stimulation analysis using Ollama.
"""

from typing import Optional
import ollama


class StimulationAnalyzer:
    """
    Analyzes text to determine a stimulation score using Ollama.
    """

    def __init__(self, host: str = "http://localhost:11434", model: str = "phi3"):
        """
        Initialize the analyzer with a connection to the Ollama client.

        Args:
            host (str): The Ollama host URL.
            model (str): The name of the model to use for analysis.
        """
        self.client = ollama.Client(host=host)
        self.model = model
        self._ensure_model_exists()

    def _ensure_model_exists(self) -> None:
        """
        Checks if the specified model is available locally and pulls it if not.
        """
        try:
            models = self.client.list()["models"]
            if not any(m["name"] == self.model for m in models):
                print(f"Model '{self.model}' not found. Pulling it now...")
                self.client.pull(self.model)
                print(f"Model '{self.model}' pulled successfully.")
        except Exception as e:
            print(f"Error checking for model '{self.model}': {e}")
            print("Please ensure Ollama is running and accessible.")
            raise

    def analyze(self, text: str) -> Optional[float]:
        """
        Analyzes the text and returns a stimulation score (0.0 to 1.0).

        Args:
            text (str): The text to analyze.

        Returns:
            Optional[float]: The stimulation score, or None if analysis fails.
        """
        prompt = f"""
        Analyze the following text for its emotional intensity and stimulation level.
        Return a single float between 0.0 (calm/neutral) and 1.0 (highly excited/agitated).
        Do not include any other text or explanation, just the float.

        Text: "{text}"
        """

        try:
            response = self.client.chat(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                options={"temperature": 0.1},
            )

            content = response["message"]["content"].strip()
            score = float(content)
            return min(max(score, 0.0), 1.0)

        except (ValueError, KeyError, IndexError) as e:
            print(f"Error parsing Ollama response: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred with Ollama: {e}")
            return None
