

import logging
from flask import Flask, render_template, session, request, jsonify, send_from_directory, copy_current_request_context

from flask_socketio import SocketIO, emit, disconnect, send
import datetime


# port = 3005

from app_settings import host, port


def time():
    now = f"{datetime.datetime.now()}"
    return now


async_mode = None

app = Flask(__name__, static_url_path='')


logss = logging.getLogger('werkzeug')
logss.disabled = True

app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, async_mode=async_mode)


# starting Route
@app.route('/')
def index():
    print("index called")
    # socketio.emit("noob",{"msg":"hi"})
    return send_from_directory('public', "index.html")


@app.route('/msg/<path:path>')
def msg(path):
    socketio.emit("message", {"msg": path})
    return send_from_directory('public', "index.html")


@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('public', path)


@socketio.on('sendmecarsfrompygame')
def sendmecarsfrompygame(getcarobj):
    print(getcarobj)

    direction = getcarobj["readytogreen"]

    socketio.emit("getnumofcars", {"direction": direction})


@socketio.on('sendbacknumcars')
def sendbacknumcars(numcarsobj):
    print(numcarsobj)

    # direction = msg["direction"]

    socketio.emit("returnnumcars", numcarsobj)


if __name__ == '__main__':
    log = "Web Server started on port "+f"{port}"+" at :"+time()
    print(log)
    socketio.run(app, host='0.0.0.0', port=port, debug=True)
