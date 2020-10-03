import cv2


import cvlib as cv

from cvlib.object_detection import draw_bbox

import matplotlib.pyplot as plt

from mq_settings import host, port


import socketio

sio = socketio.Client()


serveraddress = f'http://{host}:{port}/'

####################
# Connecting to SocketIO Server
####################

try:
    sio.connect(serveraddress)
    print(f"connected to server at {serveraddress}")

except:
    print(f"Cannot Connect to Server at {serveraddress}")


@sio.event
def connect():
    print(sio.sid)
    print(f'Connection established at {serveraddress}')


# show by matplotlib

def showmplt(outimg):
    plt.imshow(outimg)
    plt.show()

# display image by opencv


def showcv(outimg):

    while True:
        cv2.imshow("test image", outimg)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break


def printnumofcars(label):
    numberofcars = label.count('car')
    print('Number of cars in the image is ' + str(numberofcars))
    return numberofcars


def countcomobj(origimg):
    bbox, label, conf = cv.detect_common_objects(origimg)
    output_image = draw_bbox(origimg, bbox, label, conf)

    numofcars = printnumofcars(label)

    # showmplt(output_image)

    return numofcars


@sio.event
def getnumofcars(dirobj):
    direction = dirobj["direction"]
    print("checking number of cars in", direction)

    numofcars = 0

    try:
        pass

        im = cv2.imread('test.jpg')

        numofcars = countcomobj(im)

    except:
        pass

    numcarsobj = {"direction": direction, "numofcars": numofcars}

    print(numcarsobj)

    sio.emit('sendbacknumcars', numcarsobj)


@sio.event
def message(msg):
    print(msg)


####################
# Disconnected from The Server
####################

@sio.event
def disconnect():
    print('Disconnected from server')


# ####################
# # sio Wait LOOP
# ####################
sio.wait()
