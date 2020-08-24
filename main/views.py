from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    context = {'home_page': 'active'}
    return render(request, "home.html", context)

def register(request):
    context = {'register_page': 'active'}
    return render(request, "register.html", context)

def login(request):
    context = {'login_page': 'active'}
    return render(request, "login.html", context)