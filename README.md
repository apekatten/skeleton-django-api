# Skeleton Django API

Dockerized basic REST Web API based on Django, complete with user management, using only email and password.

### Installation
```
$ git clone <repo>
$ cd <repo>
$ docker-compose build
$ docker-compose run api sh -c "python manage.py createsuperuser"
$ docker-compose up
```
Please note that a unique username must be given, but is not used elsewhere.

#### Technologies
 * Django
 * Django REST Framework
 * Allauth
 * Argon2
 * Travis CI
 * PostgreSQL
 * Docker

#### TODO
 * Remove username completely, now it is just hidden
 * Add example API app
 * Test for timing attacks
 * Add throttling to login
 * Audit logging
 * Max login attempts for Django Admin
 * Change email templates
 * Fix email verification, points to wrong view
 * Add "API Docs"
 * Create setup command to replace secrets
 * Move database settings to env-file

#### Commands
 * Run unit tests and linting
   - ```docker-compose run api sh -c "python manage.py test && flake8"```
 * Create new app
   - ```docker-compose run api sh -c "python manage.py startapp appname"```
 * Make migrations for model changes
   - ```docker-compose run api sh -c "python manage.py makemigrations"```

#### Inspiration
 * https://wsvincent.com/django-rest-framework-user-authentication-tutorial/
