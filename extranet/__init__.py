from flask import Flask

app = Flask(__name__)


def start_server():
    from extranet import routes

    return app
