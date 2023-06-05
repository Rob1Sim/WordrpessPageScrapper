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
    routes = [str(rule) for rule in app.url_map.iter_rules()]

    # Affichage des routes
    for route in routes:
        print(route)
    return link_list



