#!/bin/bash
# Check if a filename is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <filename>"
  exit 1
fi

# Extract the filename from the first argument
filename="$1"

# Run chmod +x on the specified file
chmod +x "$filename"

# Perform other operations (e.g., git commands)
git add .
git commit -m "Made changes to $filename"
git push
