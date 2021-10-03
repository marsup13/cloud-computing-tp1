#/bin/bash

sudo su
source venv/bin/activate
export FLASK_APP=hello.py
flask run --host=0.0.0.0 --port=80

