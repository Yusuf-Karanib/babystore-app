#!/bin/bash
cd /home/ec2-user/babystore-app
sudo pkill -f app.py || true
sudo rm -rf venv
sudo python3 -m venv venv
sudo ./venv/bin/pip install -r requirements.txt
sudo nohup ./venv/bin/python app.py > app.log 2>&1 &