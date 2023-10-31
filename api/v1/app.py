#!/usr/bin/python3
"""creating variable 'app' instance of flask"""

from models import storage
from os import getenv
from api.v1.views import app_views
from flask import Flask, make_response, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)

cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Returns a error 404"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    if getenv('HBNB_API_HOST'):
        host = getenv('HBNB_API_HOST')
    else:
        host = '0.0.0.0'
    if getenv('HBNB_API_PORT'):
        port = getenv('HBNB_API_PORT')
    else:
        port = 5000
    app.run(host=host, port=port, threaded=True)
