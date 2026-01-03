"""
Unit tests for PulseUX Core.
"""

import pytest
from src.core.app import PulseUXTracker

@pytest.fixture
def tracker():
    return PulseUXTracker()

def test_tracker_initialization(tracker):
    """Ensure the tracker initializes with defaults."""
    assert tracker.ollama_host is not None

def test_analyze_stimulation_logic(tracker):
    """Test the heuristic logic used for the MVP."""
    # Test low stimulation
    low_score = tracker._analyze_stimulation("ok.")
    assert 0.0 <= low_score <= 0.4

    # Test high stimulation (heuristic looks for exclamation and keywords)
    high_score = tracker._analyze_stimulation("Wow! This is exciting!")
    assert high_score > 0.5
    assert high_score <= 1.0

def test_process_input_text(tracker):
    """Test public interface for text mode."""
    score = tracker.process_input("Standard input", mode="text")
    assert isinstance(score, float)

def test_process_input_voice(tracker):
    """Test public interface for voice mode (mocked)."""
    score = tracker.process_input("dummy.wav", mode="voice")
    assert isinstance(score, float)
