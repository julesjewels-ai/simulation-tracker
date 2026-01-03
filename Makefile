PYTHON = python3
VENV = venv
BIN = $(VENV)/bin

.PHONY: all install run test clean

all: install test

install:
	$(PYTHON) -m venv $(VENV)
	$(BIN)/pip install --upgrade pip
	$(BIN)/pip install -r requirements.txt
	@echo "Installation complete. Run 'make run' to start."

run:
	$(BIN)/python main.py

test:
	$(BIN)/pytest tests

clean:
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
