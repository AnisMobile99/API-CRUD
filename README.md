# API-CRUD
API-CRUD


Architecture du projet
├── app/
        ├── database.py
        ├── main.py
        ├── schemas.py
        ├── models.py


├── requirements.txt

├── test/
         ├── test_main.py
         └── test_crud.py
         └── test_database.py

Pré-requis
Vous avez besoin de sqlite pour faire marcher cette API.

Installation
Exécuter cette commande afin d'avoir toutes les librairies utilise :


Utilisation
Enfin l'installation finit, vous devez exécuter cette commande pour lancer le serveur :
python -m uvicorn main:app --reload

Rendez-vous sur le site une fois le serveur lancée a fin de voir les requêtes possibles à faire avec leur données à donner

http://127.0.0.1:8000/
Unit-Test
Pour executer les tests de l'api, suivez les intructions suivantes :

cd test/
python -m unittest -v test_api
