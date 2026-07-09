#!/bin/bash
# Convenient runner script for the Project Health Agent

# Ensure we are in the project root directory
cd "$(dirname "$0")"

# Check if Gemini API key is set
if [ -z "$GEMINI_API_KEY" ]; then
    echo "Error: GEMINI_API_KEY environment variable is not set."
    echo "Please set it before running this script:"
    echo "  export GEMINI_API_KEY=\"your_key_here\""
    echo ""
    echo "Or run the script by passing the key directly:"
    echo "  GEMINI_API_KEY=\"your_key_here\" ./run.sh"
    exit 1
fi

# Create a virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install requirements
echo "Installing/checking dependencies..."
pip install -r requirements.txt --quiet

# Run the agent
echo "Running Project Health Agent..."
python3 main.py
