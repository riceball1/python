from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    # to get this to work make sure to run `python3 manage.py makemigrations`
    # initially add 1 as an id since it already exists in the current database to the user for the foreignkey, it would break if the id is not valid
    # then `python3 manage.py migrate` to complete the migration
    # see the changes with `python3 manage.py shell`
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")