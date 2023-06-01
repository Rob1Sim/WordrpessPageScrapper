# Wordpress Page Scrapper  
Petit Tools qui s'occupe de récupérer des pages (privé ou non) d'un serveur Wordpress, les pages sont récupérer puis stocker et accesible depuis un serveur Flask.  
## Prérequis

- Python 3.6 ou une version ultérieure
- pip (le gestionnaire de paquets Python)
- Git (pour cloner le dépôt)

## Installation

1. Clonez le dépôt dans un répertoire local :
```
git clone <URL_DU_DÉPÔT>
```
2. Accédez au répertoire du projet :
```
cd WordpressPageScrapper
```
3. Créez et activez un environnement virtuel :

- Pour les systèmes Unix (Linux/macOS) :
```
python3 -m venv venv
source venv/bin/activate
```
- Pour Windows :  
```
python -m venv venv
venv\Scripts\activate
```

4. Installez les dépendances du projet :
Assurez-vous également d'inclure un fichier requirements.txt contenant les dépendances nécessaires à votre projet.
```
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
Le script utilise un serveur flask il suffit de lancer le script app.py

## Lancement Alternatif :
Une image docker peut être construite, ou récupérer sur Docker Hub :
```
docker pull robinsim1/wordpress-page-scrapper:v1.0
```