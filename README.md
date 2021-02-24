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

Go To Postman on left corner and press Import button

Select the file: ```OccurrrencesManager.postman_collection.json``` located on project base and press import

Go on right corner and press the "eye" button, and press on Add button

Create two variables, username and password. The values are the same of the user registered ( you can switch users here )

Now you are ready to enjoy testing the api!

## Endpoints List
Register: ```http://0.0.0.0:8000/api/auth/register/```

Login: ```http://0.0.0.0:8000/api/auth/login/``` (web only)

Create Occurrence: ```http://0.0.0.0:8000/api/auth/occurrences/``` POST

Get All Occurrence: ```http://0.0.0.0:8000/api/auth/occurrences/``` GET

Get Occurrence: ```http://0.0.0.0:8000/api/auth/occurrences/1/``` GET

Update Occurrence: ```http://0.0.0.0:8000/api/auth/occurrences/1/``` PUT

Delete Occurrence: ```http://0.0.0.0:8000/api/auth/occurrences/1/``` DELETE

Filter Occurrences: ```http://0.0.0.0:8000/api/occurrences/?author=2&category=1&lng=7.5556&lat=37.0109&radius=10``` GET







