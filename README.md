# annota
This project is one that was made initially for my university with some classmates, now I developed it all over again by myself improving some features and adding my personal touch

### Requirements
- Python >= 3.7
- Pipenv
- PostgreSQL >= 10

### Before starting
- Create your database in PostgresSQL.

### Config the environment
#### 1. Create your .env file
> If you already have this file, skip this step.
 ~~~
  debug = True
  secret_key = supersecretkey
  allowed_hosts = *
  db_user = valentinacano
  db_password = valentinacano
  db_name = bd_desarrollo_1
  db_host = 127.0.0.1
  db_port = 5432
  email_host = emaillhost
  email_from = emailfrom
  email_port = emailport
  email_user = emailuser
  email_password = emailpassword
  frontend_url = frontenturl
  email_use_ssl = true
  email_use_tls = false
  ~~~
#### 2. Set up the virtual environment
> If you have already installed the pipenv environment, skip step 1.
1. Installing the pipenv environment:
  ```pipenv install```
2. Running the pipenv environment:
  ```pipenv shell```

#### 3. Set up the migrations and the superuser
> If you have already created the superuser, skip step 3.
1. ```python3 manage.py makemigrations```
2. ```python3 manage.py migrate```
3. ```python3 manage.py createsuperuser```

#### 4. Run the server
1. ```python3 manage.py runserver```
2. In your browser go to localhost:8000
