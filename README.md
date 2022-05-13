
# django-api-boostrap-template

Installer un projet Django déja parametré pour la création d'api avec possibilité de créer une inteface utilisateur pour présenter votre service/projet, grâce à boostrap.




## Usages de base

1. Cloner le réferenciel
```
git clone git@github.com:alexandre-meline/django-api-boostrap-template.git
```
2. Efféctuer les migrations
```
python manage.py migrate
```
3. Créer un utilisateur : Administrateur
```
python manage.py createsuperuser
```
## Gestion des fichiers statics : css/js/images

1. Ajouter au dossier root vos fichiers statics

    A chaque ajout de fichier dans le dossier static
    vous devez éxecuter cette commande.
```
python manage.py collectstatic
```
