from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def homepage(request):
    context = {'home_page': 'active'}
    if request.method == 'POST':
        user_name       = request.POST.get('username')
        password        = request.POST.get('password')
        user = auth.authenticate(username= user_name, password= password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, f"You are logged in as @{user_name}.")
            return redirect("/")
        else:
            messages.error(request, "Incorrect username or password")
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
            messages.info(request, f"Account exists for this email with the username @{act[0].username}.")
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
        messages.success(request, f"User @{act[0].username} created successfully.")
        auth.login(request, user)
        messages.success(request, f"You are logged in as @{act[0].username}.")
        return redirect('/')
    return render(request, "account/register.html", context)

def profile(request):
    context = {'user_page': "active"}
    if request.method == "POST":
        current_user = request.user
        form = request.POST
        current_user.first_name = form.get('first_name')
        current_user.last_name = form.get('last_name')
        current_user.username = form.get('username')
        if form.get('password') != '':
            current_user.set_password(form.get('password'))
        current_user.save()
    return render(request, "account/profile.html", context)

def delete(request):
    current_user = request.user
    current_user.delete()
    logout(request)
    messages.info(request, f"@{current_user} account is deleted")
    return redirect("/")

def logout(request):
    current_user = request.user
    auth.logout(request)
    messages.success(request, f"@{current_user} has been logged out.")
    return redirect("/")
