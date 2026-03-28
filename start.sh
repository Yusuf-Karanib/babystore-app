#!/bin/bash
pip3 install -r requirements.txt
pkill -f app.py || true
nohup python3 app.py > app.log 2>&1 &