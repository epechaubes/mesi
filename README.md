# mesi

Environnement de dev :
	Connecter : activate.ps1 (powershell) / activate.bat (win cmd) - Dans "env/scripts"

Si installation de package :
	pip freeze > requirements.txt
Import des packages :
	pip install -r requirements.txt

Export/Import data :
	Export : manage.py dumpdata > db.json
	Import : manage.py loaddata db.json

PSQL :
    Connexion avec user "postgres" et mdp "admin"
    Command connexion : "psql -U [user]"
    Command list users : "\du"
    Command list databases : "\l"
    Command connect database : "\c [databasename]"
    Command list tables : "\dt"


Comptes superusers (admin interface) :
    emerick / admin
	(Attention au moteur d'authentif utilisé)

Créer super user :
	python manage.py createsuperuser

Au lancement : Custom user à faire avant le premier makemigrations