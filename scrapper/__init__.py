from flask import Flask

app = Flask(__name__)


def start_server():
    from scrapper import routes

    return app