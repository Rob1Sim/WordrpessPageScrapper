# Wordpress Page Scrapper  
Petit Tools qui s'occupe de récupérer des pages (privé ou non) d'un serveur Wordpress, les pages sont récupérer puis stocker et accesible depuis un serveur Flask.  
[Lien vers la doc](https://rob1sim.github.io/WordrpessPageScrapper/wpScrapper/scrapPages.html)
## Prérequis

- Python 3.6 ou une version ultérieure
- pip (le gestionnaire de paquets Python)
- Git (pour cloner le dépôt)

## Installation

### Avec Docker : 

1. Installer l'image :
```shell
docker pull ghcr.io/rob1sim/wordrpesspagescrapper:latest
```
2. Créer un votre fichier de configuration : 
Voir la partie [Configuration](#configuration-)
3. Lancer un conteneur :
```shell
docker run -e CONFIG_FILE=./path/to/.env ghcr.io/rob1sim/wordrpesspagescrapper:latest
```
Le serveur est lancé sur le port 5000 par défaut et sur votre adresse ip local.
En utilisant docker le serveur se relancera tous les matins à 2H pour actualiser les routes vers les pages scrapper.

#### Options: 
- Pour changer le port de sortie du serveur : 
```shell
docker run -p 8888:5000 -e CONFIG_FILE=./path/to/.env ghcr.io/rob1sim/wordrpesspagescrapper:latest
```
88888 est le port de votre machine, 5000 est le port du conteneur
- Pour récupérer les logs du serveur :
```shell
docker run -e CONFIG_FILE=./path/to/.env -v /path/to/logs:/app/logs ghcr.io/rob1sim/wordrpesspagescrapper:latest
```
### Sans Docker :

1. Clonez le dépôt dans un répertoire local :
```shell
git clone <URL_DU_DÉPÔT>
```
2. Accédez au répertoire du projet :
```shell
cd WordpressPageScrapper
```shell
3. Créez et activez un environnement virtuel :

- Pour les systèmes Unix (Linux/macOS) :
```shell
python3 -m venv venv
source venv/bin/activate
```
- Pour Windows :  
```shell
python -m venv venv
venv\Scripts\activate
```

4. Installez les dépendances du projet :
Assurez-vous également d'inclure un fichier requirements.txt contenant les dépendances nécessaires à votre projet.
```shell
pip install -r requirements.txt
```

## Configuration  
Un fichier de configuration .env doit être présent dans dans le dossier scrapper/
il doit contenir les variables suivantes : 
```
BOT_LOGIN=
BOT_PASSWORD=
URL=
```
Les 2 premiers champs corresponds aux identifiants pour le compte WP du bot, 
l'URL correspond à L'URL du site WP, il doit se terminé par /

## Lancement :  
### Avec Docker :
Le serveur est déjà lancé sur l'ip de votre réseau local

### Sans Docker :
Le script utilise un serveur flask il suffit de lancer le script app.py
#### Windows :
```shell
py app.py
```
#### Linux/MacOS :
```shell
python3 app.py
```
