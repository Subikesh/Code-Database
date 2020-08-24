from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def homepage(request):
    context = {'home_page': 'active'}
    return render(request, "home.html", context)

def register(request):
    context = {'register_page': 'active'}
    if request.method == 'POST':
        username        = request.POST.get('username')
        first           = request.POST.get('first_name')
        last            = request.POST.get('last_name')
        mail            = request.POST.get('email')
        password        = request.POST.get('password')
        
        act = User.objects.filter(email = mail)
        if act.exists():
            messages.info(request, f"Account exists for this email with the username {act[0].username}.")
            return redirect('/')

        if User.objects.filter(username = username).exists():
            messages.error(request, f"Username @{username} is already taken. Try another one.")
            return redirect("/register")
        
        user = User.objects.create_user(
            username = username,
            first_name = first,
            last_name = last, 
            email = mail,
            password = password,
        )
        user.save()
        messages.success(request, f"User {act[0].username} created successfully.")
        return redirect('/')
    return render(request, "register.html", context)
