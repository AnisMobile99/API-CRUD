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

Contenu dans chaque fichier :

main.py --> contient les quatres méthodes CRUD (get, post, put, delete)
test_main.py --> contient les différents test des méthodes CRUD
La base de donnée nommé "notes" contient la table "test" qui elle contient les données qui se présentent sour la forme :

   _id (généré automatiquement) /n
   titre
   description
   

cd test/
python -m unittest -v test_api
