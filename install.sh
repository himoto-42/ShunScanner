#!/bin/bash

# Clone the repository
git clone https://github.com/himoto-42/ShunScanner.git

# Change to the repository directory
cd ShunScanner

# Install the required Python package
pip3 install print-color

# Define the path to the user's local bin directory
BIN_PATH="$HOME/.local/bin"

# Create the bin directory if it doesn't exist, then create a symbolic link to scan.py
mkdir -p "$BIN_PATH" && ln -s "$(pwd)/scan.py" "$BIN_PATH/sscan"

# Make the script executable
chmod u+x "$BIN_PATH/sscan"

# Add BIN_PATH to PATH for different shells
SHELL_TYPE=$(basename "$SHELL")

case "$SHELL_TYPE" in
bash)
  if ! grep -q 'export PATH="$HOME/.local/bin:$PATH"' "$HOME/.bashrc"; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >>"$HOME/.bashrc"
  fi
  ;;
zsh)
  if ! grep -q 'export PATH="$HOME/.local/bin:$PATH"' "$HOME/.zshrc"; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >>"$HOME/.zshrc"
  fi
  ;;
fish)
  if ! grep -q 'set -x PATH $HOME/.local/bin $PATH' "$HOME/.config/fish/config.fish"; then
    echo 'set -x PATH $HOME/.local/bin $PATH' >>"$HOME/.config/fish/config.fish"
  fi
  ;;
*)
  echo "Unsupported shell. Please add $BIN_PATH to your PATH manually."
  ;;
esac
