import os
from dotenv import load_dotenv
import requests


class WpScrapper:
    session = None
    base_url = None

    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv('URL')

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
        base_url = self.base_url + url

        if self.session is not None:
            cookies = self.session.cookies
            page = self.session.get(base_url + url, cookies=cookies)
            content = page.content

            file_name = "./extranet/templates/result.html"

            with open(file_name, "wb") as file:
                file.write(content)

            print(f"Le fichier {file_name} a été créé avec succès.")
            return
        else:
            raise Exception("Aucune session de connexion n'a été trouver")
