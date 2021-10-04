from flask import Flask
app = Flask(__name__)

@app.route('/') # Should be set as a specific path, like '/cluster1' or '/cluster2'
def my_app():
        return {
                "instance": "cluster name",
        }

