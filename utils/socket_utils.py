from __future__ import absolute_import

from .json_utils import serialize


def get_socket_message(socket):
    while not socket.closed:
        message = socket.receive()

        if not message:
            return None
        return message


def send_ack(socket):
    socket.send(serialize({'type': 'ack'}))
