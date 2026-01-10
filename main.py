"""
PulseUX Stimulation Tracker Entry Point.

Handles command-line arguments and initializes the main application loop.
"""

import argparse
import sys
from src.core.app import PulseUXTracker


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="PulseUX: Measure user stimulation via voice/text analysis."
    )
    parser.add_argument("--version", action="version", version="PulseUX v0.1.0")
    parser.add_argument(
        "--mode",
        choices=["text", "voice"],
        default="text",
        help="Input mode: 'text' for typing, 'voice' for audio file simulation.",
    )
    parser.add_argument(
        "--input", type=str, help="Direct input string or path to audio file."
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    try:
        tracker = PulseUXTracker()
    except Exception as e:
        print(f"Initialization failed: {e}", file=sys.stderr)
        return 1

    print(f"Initializing PulseUX in [{args.mode}] mode...\n")

    try:
        if args.input:
            # Single shot mode
            score = tracker.process_input(args.input, mode=args.mode)
            tracker.visualize(score)
        else:
            # Interactive mode
            print("Type 'exit' to quit. Enter text to analyze stimulation:")
            while True:
                user_input = input("PulseUX> ")
                if user_input.lower() in ["exit", "quit"]:
                    break
                if not user_input.strip():
                    continue

                score = tracker.process_input(user_input, mode="text")
                tracker.visualize(score)

    except KeyboardInterrupt:
        print("\nExiting PulseUX.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
