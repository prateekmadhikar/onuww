import json


def serialize(obj):
    return json.dumps(obj).encode('utf-8')


class Player:

    def __init__(self, id, socket, is_creater=False):
        self.id = id
        self.socket = socket

    def __eq__(self, other):
        return self.id == other.id

    @property
    def is_alive(self):
        try:
            self.socket.send(serialize({"type": "ack"}))
            return True
        except Exception:
            return False

    def send_ack(self):
        self.socket.send(serialize({'type': 'ack'}))
