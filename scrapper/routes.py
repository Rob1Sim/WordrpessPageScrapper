from flask import render_template
from . import app
from .scrapPages import WpScrapper
from os import listdir, path

# Lancement du bot
scrap = WpScrapper()
scrap.login()

# Chargement dynamique des pages
template_files = listdir('scrapper/templates')
html_files = [file for file in template_files if file.endswith('.html')]


# Définir une fonction générique de rendu de modèle
def render_template_file(filename):
    return render_template(filename)


# Génère dynamiquement des routes en fonction des fichiers présents dans le dossier "templates"
for file in html_files:
    route_name = path.splitext(file)[0]
    app.add_url_rule(f'/{route_name}', f'render_{route_name}', render_template_file, defaults={'filename': file})


@app.route('/')
def hello_world():  # put application's code here
    html_files = [file for file in template_files if file.endswith('.html')]
    link_list = ""
    for file in html_files:
        link_list += "<a href='"+path.splitext(file)[0]+"'>"+path.splitext(file)[0]+"</a>"
    return link_list


@app.route("/scrap")
def get_scrap():
    scrap.crawl_website("annuaires/")
    return render_template('result.html')



