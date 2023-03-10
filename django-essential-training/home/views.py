from django.shortcuts import render
from datetime import datetime
# from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect

# CLASS-BASED VIEWS

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'


    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(self, request, *args, **kwargs)

class LoginInterfaceView(LoginView):
    template_name= 'home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name= 'home/logout.html'

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

# Alternative to class-based views
# def home(request):
#     # can use the third param to pass data
#     return render(request, 'home/welcome.html', {'today': datetime.today()})


# Need mixin-classes to help with adding features like authentication
class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name = 'home/authorized.html'
    login_url = "/admin"


# Alternative to class-based views
# # add login_required as a decorator to the authorized function
# # should include a redirect to login if not authorized
# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})