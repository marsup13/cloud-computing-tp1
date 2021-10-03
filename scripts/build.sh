#/bin/bash

# Python virtual env
sudo su
apt install python3-venv python3-pip
python3 -m venv venv_tp1
source venv_tp1/bin/activate
pip install Flask
deactivate
