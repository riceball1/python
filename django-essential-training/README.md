# Django Essential Training

[linkedin tutorial](https://www.linkedin.com/learning/django-essential-training/)

## Django
- A python web framework
- Project uses - python 3.8 virtualenv and django 3.2

## Getting Started

- Setup a folder called `smartnotes` run the following command: `django-admin startproject smartnotes .` 
    - creates two things: smartnotes folder and a `manage.py` file
    - two main files to use in smartnotes: `url.py` and `settings.py`
- run at root `python3 manage.py runserver`
- Adding routing
    - Add a new app to smartnotes file `settings.py` for `home` under INSTALLED_APPS
    - then in urls.py must add a pathway to import views.home to be shown when the request for `home/` is accessed
- Changes to the database by running command `python3 manage.py migrate`
- create superuser `python3 manage.py createsuperuser` -- used `username: admin, password: admin`


## Notes
- - MVT (model-view-template)
- What to make good django app?
    - should be modularized (self-contained)
- migrations  -- explains what kinds of changes a database needs to perform such as create a new table, establish a new relationship, etc
- The Django admin interface allow us to quickly and easily access data that exists in the database. This means that users and groups, you can see here, are actually tables in our database.
