#!/bin/bash
sudo python3 -m pip install -r requirements.txt
sudo pkill -f app.py || true
sudo nohup python3 app.py > app.log 2>&1 &