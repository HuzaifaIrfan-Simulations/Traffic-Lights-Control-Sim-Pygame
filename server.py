from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)



from flask_socketio import send, emit

@socketio.on('msg')
def handle_message(msg):
    print(msg)









if __name__ == '__main__':
    socketio.run(app, port=3008)

