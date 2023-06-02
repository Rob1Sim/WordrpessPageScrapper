import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from random import randint
from urllib.parse import urlparse


def get_urls_from_html(html):
    """
    Cherche dans les pages des liens vers d'autres pages
    :param html:
    :return:
    """
    soup = BeautifulSoup(html, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if url:
            url_parser = urlparse(url)
            base_url_parser = urlparse(os.getenv('URL'))
            if url_parser.netloc == base_url_parser.netloc:
                urls.append(url)
    return urls


def set_href_to_relative(content: bytes):
    """
    Modifie une page html pour changer les liens vers des liens relatifs
    :param content:
    :return: Le page modifié
    """
    soup = BeautifulSoup(content, 'html.parser')

    anchors = soup.select('a')

    for anchor in anchors:
        try:
            href = anchor['href']
            new_href = urlparse(href)
            final_path = new_href.path
            if new_href.path[-1] == "/":
                final_path = final_path[:-1]
            anchor['href'] = final_path
        except:
            continue

    return str(soup)


class WpScrapper:
    """
    Objet qui s'occupe de se connecter et d'envoyer le bot à la recherche de pages puis de les enregistrés
    """
    session = None
    base_url = None

    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv('URL')
        if self.base_url is None:
            raise Exception("Le fichier .env est manquant")

    def login(self):
        """
        Ce connecte au site WP avec les donnée du .env
        Affiche une erreur si la connexion echoue
        :return:
        """

        login_url = self.base_url + "wp-login.php"
        username = os.getenv('BOT_LOGIN')
        password = os.getenv('BOT_PASSWORD')

        login_data = {
            'log': username,
            'pwd': password,
            'wp-submit': 'Log In',
            'redirect_to': '',
            'testcookie': 1
        }

        # Récupère la session sécurisée dans cette variable
        session = requests.Session()

        response = session.post(login_url, data=login_data)

        if response.status_code != 200:
            raise Exception("Echec de connexion au site " + str(response.status_code), response.text,
                            response.status_code, response.content)

        else:
            self.session = session
            return

    def scrap_page(self, url: str):
        """
        Récupère le code HTML, CSS et JS de l'url passé en paramètre, et en créer un fichier HTML dans le dossier templates
        :param url: la sous url ../cette-url
        :param session: La session d'authentification, nécéssaire sinon la page renvoyé sera la page de connexion
        :return:
        """
        page = self.__get_page(url)
        content = page.content
        correct_content = set_href_to_relative(content)
        # Récupère le nom de l'url
        url_name = url.split('/')
        try:
            file_name = "./server/templates/page_" + url_name[-2] + ".html"
        except:
            file_name = "./server/templates/page_" + str(randint(-10000, 10000)) + str(randint(-10000, 10000)) + str(
                randint(-10000, 10000)) + ".html"

        with open(file_name, "w") as file:
            file.write(correct_content)
        print(f"Le fichier {file_name} a été créé avec succès.")
        return

    def scrap_page_to_string(self, url):
        request = self.__get_page(url)
        if request.status_code == 404:
            return False
        return self.__get_page(url).text

    def __get_page(self, url: str):
        """
        Retourne les donnée server sur une page
        :param url:
        :return:
        """
        base_url = url
        if not url.startswith('http'):
            base_url = self.base_url + url
        if self.session is not None:
            cookies = self.session.cookies
            return self.session.get(base_url + url, cookies=cookies)
        else:
            raise Exception("Aucune session de connexion n'a été trouver")

    def crawl_website(self, url):
        """
        Analize et récupère toutes les pages indexés sur un site
        :param url:
        :return:
        """
        visited_urls = set()
        urls_to_visit = [url]

        while urls_to_visit:
            current_url = urls_to_visit.pop(0)
            if current_url in visited_urls:
                continue

            html = self.scrap_page_to_string(current_url)
            if html:
                urls = get_urls_from_html(html)
                visited_urls.add(current_url)
                urls_to_visit.extend(urls)

                self.scrap_page(current_url)
