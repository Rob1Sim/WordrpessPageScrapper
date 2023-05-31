from flask import render_template
from . import app
from .scrapPages import WpScrapper
from os import listdir,path

# Lancement du bot
scrap = WpScrapper()
scrap.login()


# Chargement dynamique des pages
template_files = listdir('templates')
html_files = [file for file in template_files if file.endswith('.html')]

# Génère dynamiquement des routes en fonctions des fichier présent dans templates
for file in html_files:
    route_name = path.splitext(file)[0]

    @app.route(f'/{route_name}')
    def render_template_file():
        return render_template(file)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route("/scrap")
def get_scrap():
    scrap.scrap_page("annuaires/")
    return render_template('result.html')
