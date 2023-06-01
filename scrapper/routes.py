from flask import render_template
from . import app
from .scrapPages import WpScrapper
from os import listdir, path


def update_file_routes():
    """
    Scan les fichier présent dans templates pour en créer des routes
    :return:
    """
    template_files = listdir('scrapper/templates')
    html_files = [file for file in template_files if file.endswith('.html')]

    # Génère dynamiquement des routes en fonction des fichiers présents dans le dossier "templates"
    for file in html_files:
        route_name = path.splitext(file)[0]
        app.add_url_rule(f'/{route_name}', f'render_{route_name}', render_template_file, defaults={'filename': file})


def render_template_file(filename):
    return render_template(filename)


# Lancement du bot
scrap = WpScrapper()
scrap.login()
update_file_routes()


@app.route('/')
def hello_world():
    template_files = listdir('scrapper/templates')
    html_files = [file for file in template_files if file.endswith('.html')]
    link_list = ""
    for file in html_files:
        link_list += "<a href='" + path.splitext(file)[0] + "'>" + path.splitext(file)[0] + "</a>"
    return link_list


@app.route("/scrap")
def get_scrap():
    scrap.crawl_website("annuaires/")
    return
