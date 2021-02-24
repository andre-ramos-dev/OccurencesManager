# Occurrences Manager API Project Setup (django3.1.6/python3.7)

Build docker
 - ```docker-compose build```

Up the db container
 - ```docker-compose up postgis```
 
Up the api container
 - ```docker-compose up api```
 
Run Migrations
 - ```docker-compose exec api python manage.py migrate```

Create Base Categories
 - ```docker-compose exec api python manage.py create_categories```
 
Create admin user to access in the backoffice on ```http://0.0.0.0:8000/admin```
 - ```docker-compose exec api python manage.py createsuperuser```
 
Now you can create as many users that you desire going to users page after login


## Setup Postman
