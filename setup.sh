#! /bin/bash

sudo apt install -y libsm6 libxext6
sudo apt install -y libxrender-dev
sudo apt install mosquitto

sudo python3 -m pip install -r flask/requirements.txt
sudo python3 -m pip install -r mqtt/requirements.txt
