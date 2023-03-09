from django.urls import path

from . import views

urlpatterns = [
    # using class-based template
    path('home', views.HomeView.as_view()),
    # when not using class-based template 
    # path('home', views.home),
    
    # using class-based template
    path('authorized', views.AuthorizedView.as_view())

    #when not using class-based template
    # path('authorized', views.authorized)
]