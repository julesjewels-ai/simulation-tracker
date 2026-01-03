# PulseUX Stimulation Tracker

Local-first macOS tool using Whisper.cpp and Ollama to measure and visualize user stimulation levels via voice/text.

## Tech Stack

- Tauri
- Rust
- React
- SQLite
- Whisper.cpp
- Ollama
- CoreML

## Features

- Local Voice Transcription
- Sentiment Analysis
- Stimulation Heatmapping
- Privacy-First Storage

## Quick Start

```bash
# Clone and setup
git clone <repo-url>
cd pulseux-stimulation-tracker
make install

# Run the application
make run
```

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
make run
```

## Development

```bash
make install  # Create venv and install dependencies
make run      # Run the application
make test     # Run tests
make clean    # Remove cache files
```

## Testing

```bash
pytest tests/ -v
```
