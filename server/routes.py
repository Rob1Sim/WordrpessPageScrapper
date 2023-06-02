from flask import render_template
from . import app
from os import listdir, path


def update_file_routes():
    """
    Scan les fichier présent dans templates pour en créer des routes
    :return:
    """

    #Listes les pages et créer des routes
    template_files = listdir('server/templates')
    html_files = [file for file in template_files if file.endswith('.html')]

    # Génère dynamiquement des routes en fonction des fichiers présents dans le dossier "templates"
    for file in html_files:
        route_name = path.splitext(file)[0]
        app.add_url_rule(f'/{route_name}', f'render_{route_name}', render_template_file, defaults={'filename': file})


def render_template_file(filename):
    return render_template(filename)


# Lancement du bot

update_file_routes()


@app.route('/')
def hello_world():
    template_files = listdir('server/templates')
    html_files = [file for file in template_files if file.endswith('.html')]
    link_list = ""
    for file in html_files:
        link_list += "<a href='" + path.splitext(file)[0] + "'>" + path.splitext(file)[0] + "</a>"
    return link_list



