from flask import Flask, current_app
from flask_cors import CORS
from flask_socketio import SocketIO, emit


app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)
app.debug = True

@app.route('/')
def index():
    return 'hi'
    
if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port='5000')