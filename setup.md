# setup

### clone the repository
```
git clone git@github.com:shivapittala19/Django-ipl-project.git
```

### Install and activate the python virtual environment
```
python -m venv venv-name
source venv-name/bin/activate
```


### Install the requirements
```
pip install requirements.txt
```

# Database Connection

### create a dabase with name 'django_ipl_database'
Open your psql shell
```
create database django_ipl_database;
```
### Make sure the owner of the dabase is postgres.

```
alter database django_ipl_database owner_to postgres;
```
configure the password of the user in the setting file as per your postgres user password
 
### Run the database Migrations
```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Load the data into database 
Place the csv files required in the base folder.-
```
python3 manage.py import_dataset.py
```
### Run the server

```
python3 manage.py runserver
```

# Django Admin

### create a super user to login into admin
```
python3 manage.py createsuperuser
```
Login to the admin panel with your credentials,It has two models.You can add new objects, delete objects, and also update.

# Testing URL's

In web browser open url 
```
http://localhost:8000/api/v1/swagger/schema/
```
It will be give the API documentation of the project now you can run the respective url to test.

Changing the code to just demo