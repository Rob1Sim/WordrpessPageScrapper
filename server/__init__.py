"""
Serveur web qui met à disposition les pages téléchargés
"""
from flask import Flask, render_template
from os import listdir, path


def update_file_routes():
    """
    Scan les fichier présent dans templates pour en créer des routes
    :return:
    """

    # Listes les pages et créer des routes
    template_files = listdir('server/templates')
    html_files = [file for file in template_files if file.endswith('.html')]

    # Génère dynamiquement des routes en fonction des fichiers présents dans le dossier "templates"
    for file in html_files:
        route_name = path.splitext(file)[0]
        app.add_url_rule(f'/{route_name}', f'render_{route_name}', render_template_file, defaults={'filename': file})


def render_template_file(filename):
    return render_template(filename)


app = Flask(__name__)


def start_server():
    update_file_routes()

    from server import routes

    return app
