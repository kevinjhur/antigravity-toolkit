#!/bin/bash
# Antigravity Toolkit Setup Script for Unix (macOS/Linux)

echo "Checking Python 3 installation..."
if command -v python3 &>/dev/null; then
    PYTHON_CMD="python3"
elif command -v python &>/dev/null; then
    PYTHON_CMD="python"
else
    echo "Error: Python 3 is required but not installed."
    exit 1
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
$PYTHON_CMD "$SCRIPT_DIR/setup.py" "$@"
