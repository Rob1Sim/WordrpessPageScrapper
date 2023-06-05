from flask import render_template
from . import app
from os import listdir, path





@app.route('/')
def index():
    template_files = listdir('server/templates')
    html_files = [file for file in template_files if file.endswith('.html')]
    link_list = ""
    for file in html_files:
        link_list += "<a href='" + path.splitext(file)[0] + "'>" + path.splitext(file)[0] + "</a>"

    return link_list



