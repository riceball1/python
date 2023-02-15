from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.decorators import login_required

def home(request):
    # can use the third param to pass data
    return render(request, 'home/welcome.html', {'today': datetime.today()})

# add login_required as a decorator to the authorized function
# should include a redirect to login if not authorized
@login_required(login_url='/admin')
def authorized(request):
    return render(request, 'home/authorized.html', {})