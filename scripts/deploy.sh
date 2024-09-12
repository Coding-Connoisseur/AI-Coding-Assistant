#!/bin/bash

# deploy.sh
# This script automates the deployment process for the AI assistant project.

# Step 1: Check for uncommitted changes
if [[ $(git status --porcelain) ]]; then
  echo "There are uncommitted changes. Please commit or stash them before deploying."
  exit 1
fi

# Step 2: Pull the latest changes from the remote repository
echo "Pulling latest changes from remote..."
git pull origin main

# Step 3: Run tests before deploying
echo "Running tests..."
python -m unittest discover tests

if [ $? -ne 0 ]; then
  echo "Tests failed. Aborting deployment."
  exit 1
fi

# Step 4: Push changes to the remote repository
echo "Pushing changes to the remote repository..."
git push origin main

# Step 5: Deploy the application to the production server
echo "Deploying the AI assistant to production..."
# Assuming deployment is done using a service like Docker, AWS, etc.
# Example Docker command:
# docker build -t ai-assistant:latest .
# docker run -d -p 5000:5000 ai-assistant:latest

echo "Deployment complete."
