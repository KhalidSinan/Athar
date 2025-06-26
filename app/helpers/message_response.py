from flask import jsonify


def message_response(message, status_code=200):
    return jsonify({"message": message}), status_code
