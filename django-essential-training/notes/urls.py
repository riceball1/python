from django.urls import path

from . import views

# make sure to add it to main project urls.py folder -- in this case smartnotes

urlpatterns = [

    path('notes', views.NotesListView.as_view()),
    # non class-based view
    # path('notes', views.list),


    # path for getting specific note
    # path('notes/<int:pk>', views.detail)
    path('notes/<int:pk>', views.NotesDetailView.as_view())
]
