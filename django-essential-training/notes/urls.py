from django.urls import path

from . import views

# make sure to add it to main project urls.py folder -- in this case smartnotes

urlpatterns = [
    path('notes', views.list)
]