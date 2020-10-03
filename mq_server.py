

import logging
from flask import Flask, render_template, session, request, jsonify, send_from_directory, copy_current_request_context

from flask_socketio import SocketIO, emit, disconnect, send
import datetime



##############################################################################################################
#########################################  Setup Django Database Models and Settings  ###################################
##############################################################################################################

# import sys
# import os

# sys.path.append(os.path.join(os.path.dirname(__file__), "video_feed"))

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "video_feed.settings")
# import django
# from django.conf import settings

# django.setup()

# from app.models import Media_Pages, All_Videos





# port = 3005

from mq_settings import host, port



def time():
    now = f"{datetime.datetime.now()}"
    return now


async_mode = None

app = Flask(__name__, static_url_path='')


logss = logging.getLogger('werkzeug')
logss.disabled = True

app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app, async_mode=async_mode)



# from flask_mongoengine import MongoEngine


# app.config['MONGODB_SETTINGS'] = {
#     'db': 'traffic_control',
#     'host': 'localhost',
#     'port': 27017
# }
# db = MongoEngine()
# db.init_app(app)

# class User(db.Document):
#     name = db.StringField()
#     email = db.StringField()

# User(name='laura', email='laura@gmail.com').save()

publicfolder="public"

# starting Route
@app.route('/')
def index():
    print("index called")
    # socketio.emit("noob",{"msg":"hi"})
    return render_template("base.html")
    # return send_from_directory(publicfolder, "index.html")


@app.route('/msg/<path:path>')
def msg(path):
    socketio.emit("message", {"msg": path})
    return send_from_directory(publicfolder, "index.html")


@app.route('/<path:path>')
def send_file(path):
    return send_from_directory(publicfolder, path)


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
