from __future__ import absolute_import

from ..utils import serialize


class SocketHolder:

    def __init__(self, id, socket):
        self.id = id
        self.socket = socket

    @property
    def is_alive(self):
        try:
            self.socket.send(serialize({"type": "ack"}))
            return True
        except Exception:
            return False

    def send_ack(self):
        self.socket.send(serialize({'type': 'ack'}))
