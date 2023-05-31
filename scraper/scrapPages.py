import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup


def get_urls_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        url = link.get('href')
        if url:
            urls.append(url)
    return urls


class WpScrapper:
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

        # Récupère la session sécurisé dans cette variable
        session = requests.Session()

        response = session.post(login_url, data=login_data)

        if response.status_code != 200:
            raise Exception("Echec de connexion au site " + str(response.status_code), response.text,
                            response.status_code, response.content)

        else:
            self.session = session
            return

    def scrap_page(self, url):
        """
        Récupère le code HTML, CSS et JS de l'url passé en paramètre, et en créer un fichier HTML dans le dossier templates
        :param url: la sous url ../cette-url
        :param session: La session d'authentification, nécéssaire sinon la page renvoyé sera la page de connexion
        :return:
        """
        page = self.__get_page(url)
        content = page.content

        file_name = "./scraper/templates/result.html"

        with open(file_name, "wb") as file:
            file.write(content)
        print(f"Le fichier {file_name} a été créé avec succès.")
        return

    def scrap_page_to_string(self, url):
        return self.__get_page(url).text

    def __get_page(self, url):
        """
        Retourne les donnée scrapper sur une page
        :param url:
        :return:
        """
        base_url = self.base_url + url
        if self.session is not None:
            cookies = self.session.cookies
            return self.session.get(base_url + url, cookies=cookies)
        else:
            raise Exception("Aucune session de connexion n'a été trouver")

    def crawl_website(self,url):
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
            urls = get_urls_from_html(html)
            visited_urls.add(current_url)
            urls_to_visit.extend(urls)

            print(current_url)
