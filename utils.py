import json


def serialize(obj):
    return json.dumps(obj).encode('utf-8')


def deserialize(str):
    try:
        return json.loads(str.decode('utf-8'))
    except Exception:
        return str
