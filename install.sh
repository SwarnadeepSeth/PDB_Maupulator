#!/bin/bash

# Determine the directory where the install.sh script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Ensure the pdbM.py script is executable
chmod +x "$SCRIPT_DIR/src/pdbM.py"

# Remove the existing symbolic link, if any
sudo rm -f /usr/local/bin/pdbM

# Create a new symbolic link to pdbM.py in /usr/local/bin
sudo ln -s "$SCRIPT_DIR/src/pdbM.py" /usr/local/bin/pdbM

echo "pdbM has been installed successfully and is now available in /usr/local/bin"
