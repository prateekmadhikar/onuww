import httplib

from flask import jsonify


def JSONResponse(data, status_code=httplib.OK):
    response = jsonify(data)
    response.status_code = status_code

    return response
