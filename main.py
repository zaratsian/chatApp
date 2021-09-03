from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xyzchatapp123'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('event')
def handle_my_custom_event(json_payload, methods=['GET', 'POST']):
    #print(f'Received event: {json_payload}')
    emit('response', json_payload)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=8080, debug=True)


