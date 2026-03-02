#!/bin/bash
# Install deps
apt install python3-pip -y
apt install python3-venv -y

# Install package deps
sudo apt install python3-flask python3-opencv

# Create venv
python3 -m venv venv

# Activate venv
source venv/bin/activate

# Install python deps
pip install -r requirements.txt