from flask import Flask



app = Flask(__name__)


def start_server():
    from server import routes

    return app
