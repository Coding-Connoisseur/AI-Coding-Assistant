#!/bin/bash

# setup_env.sh
# This script sets up the environment for the AI assistant project.

# Step 1: Create a Python virtual environment
echo "Creating a virtual environment..."
python3 -m venv venv

# Step 2: Activate the virtual environment
echo "Activating the virtual environment..."
source venv/bin/activate

# Step 3: Install required dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Step 4: Set environment variables (OpenAI API Key)
echo "Setting up environment variables..."
export OPENAI_API_KEY="your_openai_api_key"

# Step 5: Confirm setup
echo "Environment setup complete. Virtual environment activated, and dependencies installed."
