#!/bin/bash
BIN_PATH="$HOME/.local/bin"
REPO_DIRNAME="ShunScanner"

# Clone the repository
git clone https://github.com/himoto-42/ShunScanner.git

# Change to the repository directory
cd $REPO_DIRNAME

# Create the bin directory if it doesn't exist, then put command
mkdir -p "$BIN_PATH" && cp "$(pwd)/scan.py" "$BIN_PATH/sscan"

# Make the script executable
chmod u+x "$BIN_PATH/sscan"

# Delete repo
cd .. && rm -rf $REPO_DIRNAME
