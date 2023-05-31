from flask import render_template
from . import app
from .scrapPages import WpScrapper

scrap = WpScrapper()
scrap.login()


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route("/scrap")
def get_scrap():
    scrap.scrap_page("annuaires/")
    return render_template('result.html')
