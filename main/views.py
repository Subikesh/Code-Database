from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def homepage(request):
    context = {'home_page': 'active'}
    return render(request, "home.html", context)

def register(request):
    context = {'register_page': 'active'}
    if request.method == 'POST':
        user            = request.POST.get('username')
        first           = request.POST.get('first_name')
        last            = request.POST.get('last_name')
        mail            = request.POST.get('email')
        password        = request.POST.get('password')
        if User.objects.filter(email = mail).exists():
            print("Account exist with this email. Please Login.")
            return redirect('/login')
        if User.objects.filter(username = user).exists():
            print("Username taken")
            return render(request, "register.html", context)
        user = User.objects.create_user(
            username = user,
            first_name = first,
            last_name = last, 
            email = mail,
            password = password,
        )
        user.save()
        print("User created successfully")
        return redirect('/')
    return render(request, "register.html", context)

def login(request):
    context = {'login_page': 'active'}
    return render(request, "login.html", context)