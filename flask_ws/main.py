import logging

from flask import Flask, render_template
from flask_socketio import SocketIO

# socketIO settings
app = Flask(__name__)
socketio = SocketIO(app)

# logging settings
gunicorn_logger = logging.getLogger("gunicorn.error")
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)


@app.route("/")
def hello_world():
    return render_template("index.html")


@socketio.on("my event")
def handle_message(data):
    app.logger.info(f"received message: {str(data)}")


@socketio.on("connect")
def test_connect(auth):
    app.logger.info(f"connected: {str(auth)}")


@socketio.on("disconnect")
def test_disconnect():
    app.logger.info(f"disconnected")


if __name__ == "__main__":
    socketio.run(app)
