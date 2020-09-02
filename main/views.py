from django.shortcuts import get_object_or_404, render, redirect
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
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in.")
        return redirect('/')
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
    if not request.user.is_authenticated:
        messages.error(request, "You are not logged in yet.")
        return redirect("/")
    current_user = request.user
    auth.logout(request)
    messages.success(request, f"@{current_user} has been logged out.")
    return redirect("/")

# Editing and updating user information
def profile(request):
    if not request.user.is_authenticated:
        messages.error(request, "You are not logged in yet.")
        return redirect("/")
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
    if not request.user.is_authenticated:
        messages.error(request, "You are not logged in yet.")
        return redirect("/")
    current_user = request.user
    current_user.delete()
    logout(request)
    messages.error(request, f"@{current_user} account is deleted")
    return redirect("/")

# Adding a new question or editing an existing question
def add_question(request, question_id = None):
    if not request.user.is_authenticated:
        messages.error(request, "Please Login to add question.")
        return redirect("/")
    context = {}
    context['option'] = "Edit" if question_id else "Add"
    question = get_object_or_404(models.Question, pk=question_id) if question_id else None
    if request.method == "POST":
        form = QuestionForm(request.POST, user=request.user, instance=question)
        if form.is_valid():
            if not question_id:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
            else:
                form.save()
            messages.success(request, f"Question {request.POST.get('title')} is saved")
        else:
            for error in form.errors.values():
                messages.error(request, error.as_text()[2:])
    else:
        form = QuestionForm(instance=question)
    fields = dict(zip(form.fields.keys(), form))
    context["fields"] = fields
    context["form"] = form
    return render(request, "questions/question.html", context)

# View full details of the question
def view_question(request, question_id):
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to view questions")
        return redirect("/")
    context = {}
    question = get_object_or_404(models.Question, pk=question_id)
    solutions = models.Solution.objects.filter(question = question)
    if request.method == "POST":
        title           = request.POST.get('soln-title')
        if not title:
            title = "Solution " + str(len(solutions)+1)
        description     = request.POST.get('soln-desc')
        language        = request.POST.get('language')
        code            = request.POST.get('code')
        link            = request.POST.get('link')
        new_solution = models.Solution(
            question    = question,
            title       = title, 
            language    = language,
            program     = code,
            notes       = description,
            link        = link
        )
        new_solution.save()
        solutions |= models.Solution.objects.filter(pk=new_solution.pk)
    context['question'] = question
    context['solutions'] = solutions    
    return render(request, "questions/display_question.html", context)
