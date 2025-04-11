import socketio


sio = socketio.Client()
def start():
    sio.connect()

@sio.event
def connect():
    print("life")