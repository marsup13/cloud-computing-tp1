# TP1

## Instance setup
All the following commands should be run as **root user**.
```
sudo su
```
### Initial
Please run the script if instances just built.
Otherwise, this could be ignored.
```
apt update && apt upgrade -y
```

### Install package
```
apt install python3-venv python3-pip -y
pip install Flask
```

### Execute Flask
Please set up the correct route in `hello.py` in advance.
```
export FLASK_APP=hello.py
flask run --host=0.0.0.0 --port=80
```