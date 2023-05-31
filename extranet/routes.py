from flask import render_template
from . import app


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')
