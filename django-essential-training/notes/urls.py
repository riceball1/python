from django.urls import path

from . import views

# make sure to add it to main project urls.py folder -- in this case smartnotes

urlpatterns = [

    path('notes', views.NotesListView.as_view(), name="notes.list"),
    # non class-based view
    # path('notes', views.list),


    # path for getting specific note
    # path('notes/<int:pk>', views.detail)
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),

    # path for updating notes
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.update"),

    # path for deleting notes
    path('notes/<int:pk>/delete', views.NotesDeleteView.as_view(), name="notes.delete"),


    # path to create new notes
    path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),
]
