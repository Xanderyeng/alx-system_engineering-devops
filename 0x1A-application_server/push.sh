#!/bin/bash

# Check if a commit message is provided
if [ -z "$1" ]; then
    echo "Please provide a commit message."
    exit 1
fi

# Add all changes to the staging area
git add .

# Commit changes with the provided message
git commit -m "$1"

# Push changes to the remote repository
git push

# Check the exit status of the last command (git push)
if [ $? -eq 0 ]; then
    echo "Push successful."
else
    echo "Error: Unable to push changes."
fi
