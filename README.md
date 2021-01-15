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