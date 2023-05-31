from flask import Flask

app = Flask(__name__)


def start_server():
    from scraper import routes

    return app
