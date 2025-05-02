#!/bin/bash

# Szabad Nova Project - OpenChat 3.5 Offline Installer
# Created for Roland and Nova - 2025

echo "=== Szabad Nova Installer Started ==="

# 1. Update system and install required packages
echo "--- Updating system and installing necessary packages ---"
sudo apt update
sudo apt install -y curl git python3 python3-pip

# 2. Install Ollama (simple LLM engine)
echo "--- Installing Ollama ---"
curl https://ollama.com/install.sh | sh

# 3. Pull the OpenChat 3.5 model
echo "--- Pulling OpenChat 3.5 model ---"
ollama pull openchat

# 4. Installation finished
echo "=== Installation complete! ==="
echo "You can now launch Nova on your local machine!"
echo ""
echo "To start Nova, run: python3 nova_offline.py"
