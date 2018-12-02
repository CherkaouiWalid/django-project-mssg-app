from django.http import  HttpResponseRedirect
from django.contrib.auth.models import User

def index(request):
    if (not User.is_authenticated):
        return HttpResponseRedirect('/accounts/login')
    else:
        return HttpResponseRedirect('/msg')