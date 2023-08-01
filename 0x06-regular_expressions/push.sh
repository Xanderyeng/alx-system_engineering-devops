#!/bin/bash
# Extract the filename from the first argument
filename="$1"

# Run chmod +x on the specified file
#chmod +x "$filename"

# Perform other operations (e.g., git commands)
git add .
git commit -m "Made changes to $filename"
git push
