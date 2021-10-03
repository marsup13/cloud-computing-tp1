from flask import Flask
app = Flask(__name__)

@app.route('/') # Should be set to specific path, like '/cluster1'
def my_app():
        return 'First Flask application!\n'
