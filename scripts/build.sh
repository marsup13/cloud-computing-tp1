#/bin/bash

# Python virtual env
sudo apt install python3-venv
mkdir venv_tp1 && cd venv_tp1
python3 -m venv venv
source venv/bin/activate
sudo su
pip install Flask

