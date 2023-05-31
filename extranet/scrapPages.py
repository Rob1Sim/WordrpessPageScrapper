import os
from dotenv import load_dotenv
import requests


load_dotenv()

# Récupère les données stocké dans la varialble d'environnement URL
url = os.getenv('URL')

login_url = url + "wp-login.php"
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
    print("Echec de connexion au site " + str(response.status_code))
else:
    page = session.get(url)
    content = response.content

    # Nom du fichier de destination
    file_name = "result.html"

    # Chemin complet du fichier

    # Écriture du contenu de la réponse dans le fichier
    with open(file_name, "wb") as file:
        file.write(content)

    print(f"Le fichier {file_name} a été créé avec succès.")