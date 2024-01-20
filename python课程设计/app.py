from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
import logging


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:8080", "http://192.168.31.164:8080", "http://192.168.31.164:5001"]}})
socketio = SocketIO(app, cors_allowed_origins=["http://localhost:8080", "http://192.168.31.164:8080", "http://192.168.31.164:5001"])
logging.basicConfig(level=logging.DEBUG)


@app.route('/api/push-ups', methods=['GET'])
def get_push_ups_data():
    # 调用 push-ups.py 中的功能
    # 返回数据
    data = {"push_ups": "some data from push-ups.py"}
    return jsonify(data)


@socketio.on('connect')
def handle_connect():
    print('Client connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001, debug=True, use_reloader=False)
