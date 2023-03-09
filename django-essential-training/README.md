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

## How Django Interacts with Databases

- ORMs
    - Django has pre-defined user models, but you can create your own models.
    - Django uses an object relational mapping system (ORM) to communicate with the database and handle changes.
    - To create a model, you write a class with attributes that represent columns in the database table.
    - Migrations are used to transform a model into a database table, and each migration specifies the changes to be made in the database.
    - The "migrate" command applies migrations to the database, while the "make migrations" command creates migration space in the code.
    - The ORM handles the process of creating a model, creating a migration, applying the migration to the database, and making changes.
    - Django's ORM is considered one of the best for Python and SQL databases.
    - Can use the command `python3 manage.py makemigrations` to make migrations which creates a set of instructions, then use `python3 manage.py migrate` to apply the migrations to the database

- Django shell
    - access by using `python3 manage.py shell` -- opens an interpreter tightly coupled with project
    ```python
    from notes.models import Notes
    mynote = Notes.objects.get(pk='1')

    In [3]: mynote.title
    Out[3]: 'Django Tutorial'

    In [4]: mynote.text
    Out[4]: 'Get started with django'

    # get all notes
    Notes.objects.all() # <QuerySet [<Notes: Notes object (1)>]>

    # create new note
    new_note = Notes.objects.create(title="new note", text="this is a new note")

    # search for notes
    Notes.objects.filter(title__startswith="Django" #  <QuerySet [<Notes: Notes object (1)>]>


    ```


## Building Dynamic Webpages

- Needs to create a urlpattern for the path, and include it also in the main project's `urls.py` file
- Needs to create `template/< name of subfolder>/` then a file for the template using `html` extension


## Building a Robust Frontend in Django
    - add static files to be able to inject css styles
    - use a base template to make this easier
        - use a base.html
## Django Forms: Validation Shouldn't Be Hard
    - CreateView method
    - adding a form using `{{form}}` and to ensure able to perform the POST need to add `{{% csrf_token %}}`, which stands for `cross-site request forgery`

- Cross-site request forgery (CSRF) is a type of security vulnerability that can occur in web applications, including those built with Django. A CSRF attack happens when an attacker tricks a user into unknowingly performing an action on a website without their consent or knowledge
- In Django, CSRF attacks can be prevented by using a built-in middleware called "CsrfViewMiddleware". This middleware provides protection by generating a unique token for each user session and including it in every form submission. When a user submits a form, Django checks that the token in the request matches the one in the session. If they don't match, the request is considered invalid and Django rejects it.
- To ensure that your Django application is protected against CSRF attacks, you should make sure that the "CsrfViewMiddleware" is included in your middleware settings, and that all forms in your application include the CSRF token using the {% csrf_token %} template tag.

## Working with Existing Data
## Using Django to Store and Display User-Specific Data
## Login, Logout, and Signup Are Simple