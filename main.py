from flask import Flask
from flask import request, jsonify, make_response
from errorWriter import errorWriter
from authenticationProcess import checkRequestData

app = Flask(__name__)


@app.route('/v1/key', methods=['POST'])
def user():
    try:
        keyRequest = request.json

        key = checkRequestData(keyRequest)
        return make_response(jsonify(key), 201)
    except Exception as e:
        error = errorWriter(400, str(e))
        return make_response(jsonify(error), 400)


@app.errorhandler(404)
def route_not_found(e):
    error = errorWriter(404, str(e))
    return make_response(jsonify(error), 404)


if __name__ == '__main__':
    app.run()
