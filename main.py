
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xyzantidote123'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    #socketio.emit('my response', json, callback=messageReceived)
    emit('my response', json)

if __name__ == '__main__':
    socketio.run(app, debug=True)


