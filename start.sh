#!/bin/bash
pip3 install -r requirements.txt
pkill -f app.py || true
sudo nohup python3 app.py > app.log 2>&1 &