from flask import Flask
from flask_sockets import Sockets

app = Flask(__name__)
app.debug = True
socket = Sockets(app)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World', 200


# Uncomment the following to run locally and run 'python app.py' from the root folder
# if __name__ == "__main__":
#     from gevent import pywsgi
#     from geventwebsocket.handler import WebSocketHandler
#     server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
#     server.serve_forever()
