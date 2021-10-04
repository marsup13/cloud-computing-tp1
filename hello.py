from flask import Flask
app = Flask(__name__)

@app.route('/') # Should be set to specific path, like '/cluster1' or 'cluster2'
def my_app():
        return {
                "instance": "cluster name",
        }

