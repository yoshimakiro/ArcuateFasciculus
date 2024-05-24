#!/bin/bash

# Function to print an error message and exit
function error_exit {
    echo "$1" 1>&2
    exit 1
}

# Create a virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    python3 -m venv venv || error_exit "Failed to create virtual environment."
fi

# Activate the virtual environment
source venv/bin/activate || error_exit "Failed to activate virtual environment."

# Install dependencies
pip install -r requirements.txt || error_exit "Failed to install dependencies."

# Set environment variables
export OPENAI_API_KEY=${OPENAI_API_KEY}

# Inform the user
echo "Setup complete. Virtual environment activated and dependencies installed."
echo "Remember to source this script whenever you start working on the project:"
echo "source ./setup.sh"
