import uuid
import json
from django.http import HttpResponse, HttpResponseBadRequest
from datetime import datetime

class Encoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        else:
            return obj


def httpResponseBadRequest(error_description, message="UNEXPECTED ERROR", status_code=200):
    ret = {}
    ret["status"] = False
    ret["error"] = message
    ret['error_description'] = error_description if type(
        error_description) is str else error_description.args[0]
    return HttpResponseBadRequest(json.dumps(ret), status=status_code, content_type="application/json")


def httpResponse(data, status=True, status_code=200):
    ret = {}
    ret["status"] = status
    ret["status_code"] = status_code
    ret["data"] = {'message': data} if type(data) is str else data
    json_ = json.dumps(ret, cls=Encoder)
    return HttpResponse(json_, status=status_code, content_type="application/json")


def validate_data(data, attributes):
    missing = []
    for attribute in attributes:
        if attribute not in data:
            missing.append(attribute)

def percentage_validation(s):
    if s>100:
            return "rating should not exceeded value 100"