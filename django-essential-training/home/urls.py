from django.urls import path

from . import views

urlpatterns = [
    # using class-based template
    path('', views.HomeView.as_view(), name="home"),
    # when not using class-based template 
    # path('home', views.home),
    
    # using class-based template
    # path('authorized', views.AuthorizedView.as_view(), name="admin"),

    #when not using class-based template
    # path('authorized', views.authorized)

    # login class-based view
    path('login', views.LoginInterfaceView.as_view(), name="login"),

     # login class-based view
    path('logout', views.LogoutInterfaceView.as_view(), name="logout"),

    # register class-based view
    path('signup', views.SignupView.as_view(), name="signup"),
]