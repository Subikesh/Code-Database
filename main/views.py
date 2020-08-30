from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django import forms
from .forms import QuestionForm
from . import models
import urllib

# Display the main content and user login page
def homepage(request):
    context = {'home_page': 'active'}
    if request.user.is_authenticated:
        # Home page after logged in
        context['questions'] = models.Question.objects.filter(user=request.user)
    else:
        # Home page to let user login
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

# User registration and validation username and email. 
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

# User logout
def logout(request):
    current_user = request.user
    auth.logout(request)
    messages.success(request, f"@{current_user} has been logged out.")
    return redirect("/")

# Editing and updating user information
def profile(request):
    context = {'user_page': "active"}
    if request.method == "POST":
        current_user = request.user
        form = request.POST
        current_user.first_name = form.get('first_name')
        current_user.last_name  = form.get('last_name')
        current_user.username   = form.get('username')
        if form.get('password') != '':
            current_user.set_password(form.get('password'))
        current_user.save()
    return render(request, "account/profile.html", context)

# Deleting user account
def delete(request):
    current_user = request.user
    current_user.delete()
    logout(request)
    messages.info(request, f"@{current_user} account is deleted")
    return redirect("/")

def add_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST, user=request.user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, f"Question {request.POST.get('title')} is saved")
        else:
            for error in form.errors.values():
                messages.error(request, error.as_text()[2:])
    else:
        form = QuestionForm()
    fields = dict(zip(form.fields.keys(), form))
    return render(request, "question.html", {"fields": fields, "form":form})

def view_question(request, question_id):
    context = {}
    try:
        question = models.Question.objects.get(pk=question_id)
        solutions = models.Solution.objects.filter(question = question)
        context['question'] = question
        context['solutions'] = solutions
    except models.Question.DoesNotExist:
        raise Http404(f"Question {question_id} does not exist.")
    return render(request, "display_question.html", context)
