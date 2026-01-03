"""
Unit tests for PulseUX Core.
"""

import pytest
from unittest.mock import patch, MagicMock
from src.core.app import PulseUXTracker


@pytest.fixture
@patch("src.core.app.StimulationAnalyzer")
@patch("src.core.app.AudioTranscriber")
def tracker(MockAudioTranscriber, MockStimulationAnalyzer):
    """Fixture to provide a mocked PulseUXTracker instance."""
    # Create mock instances from the patched classes
    mock_transcriber_instance = MockAudioTranscriber.return_value
    mock_analyzer_instance = MockStimulationAnalyzer.return_value

    # Instantiate the tracker, which will now use the mocked components
    tracker_instance = PulseUXTracker()

    # Attach mocks to the instance for easy access in tests
    tracker_instance.transcriber = mock_transcriber_instance
    tracker_instance.analyzer = mock_analyzer_instance

    return tracker_instance


def test_tracker_initialization(tracker):
    """Ensure the tracker initializes with mocked components."""
    assert tracker.analyzer is not None
    assert tracker.transcriber is not None
    assert isinstance(tracker.analyzer, MagicMock)
    assert isinstance(tracker.transcriber, MagicMock)


def test_process_input_text(tracker):
    """Test public interface for text mode with mocked analysis."""
    tracker.analyzer.analyze.return_value = 0.75

    score = tracker.process_input("This is a test", mode="text")

    assert score == 0.75
    tracker.analyzer.analyze.assert_called_once_with("This is a test")


def test_process_input_voice(tracker):
    """Test public interface for voice mode with mocked transcription and analysis."""
    tracker.transcriber.transcribe.return_value = "Transcribed text"
    tracker.analyzer.analyze.return_value = 0.85

    score = tracker.process_input("dummy.wav", mode="voice")

    assert score == 0.85
    tracker.transcriber.transcribe.assert_called_once_with("dummy.wav")
    tracker.analyzer.analyze.assert_called_once_with("Transcribed text")


def test_transcription_failure(tracker):
    """Test that a transcription failure returns a score of 0.0."""
    tracker.transcriber.transcribe.return_value = None

    score = tracker.process_input("bad.wav", mode="voice")

    assert score == 0.0
    tracker.analyzer.analyze.assert_not_called()
