from flask import Flask
app = Flask(__name__)

@app.route('/<path:text>', methods=['GET']) 
def my_app(text):
    if text.startswith('cluster'):
        return {
                "instance": "cluster name", # specify what should be return
        }

