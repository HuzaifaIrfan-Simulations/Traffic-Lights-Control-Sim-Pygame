


from flask import Flask, render_template, session, request,jsonify, send_from_directory, copy_current_request_context

from flask_socketio import SocketIO, emit, disconnect,send
import datetime


port=3005

def time():
    now = f"{datetime.datetime.now()}"
    return now


async_mode = None

app = Flask(__name__, static_url_path='')


import logging
logss = logging.getLogger('werkzeug')
logss.disabled = True

app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, async_mode=async_mode)


#starting Route
@app.route('/')
def index():
    emit("response",{"msg":"hi"}, namespace='/app')
    return send_from_directory('public', "index.html")


@app.route('/<path:path>')
def send_file(path):
    return send_from_directory('public', path)



@socketio.on('msg' , namespace='/app')
def handle_message(msg):
    print(msg)









if __name__ == '__main__':
    log="Web Server started on port "+f"{port}"+" at :"+time()
    print(log)
    socketio.run(app,host='0.0.0.0', port=port, debug=True)

