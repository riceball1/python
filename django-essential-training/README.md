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
- MVT (model-view-template)