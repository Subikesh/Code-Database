from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django import forms
from .forms import QuestionForm
from .models import Question, Solution, Tag

# Display the questions specific to user or the user login page
def homepage(request):
    context = {'home_page': 'active'}
    if request.user.is_authenticated:
        # Home page after logged in
        final_questions = Question.objects.filter(user = request.user).order_by('-date_added')
        search          = request.GET.get('search')
        difficulty      = request.GET.get('difficulty')
        tag             = request.GET.get('tag')
        if search:
            final_questions = final_questions.filter(title__icontains = search)
        if difficulty:
            final_questions = final_questions.filter(difficulty = difficulty)
        if tag:
            final_questions = final_questions.filter(tag__pk = tag)
        context['questions'] = final_questions[:20]
        context['tags'] = Tag.objects.all()
    else:
        # Home page for user login 
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
    question = get_object_or_404(Question, pk=question_id) if question_id else None
    if request.method == "POST":
        form = QuestionForm(request.POST, user=request.user, instance=question)
        if form.is_valid():
            if not question_id:
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                form.save_m2m()
            else:
                form.save()
            messages.success(request, f"Question {request.POST.get('title')} is saved")
        else:
            for error in form.errors.values():
                messages.error(request, error.as_text()[2:])
        if question_id:
            return redirect(f"/questions/{question_id}")
    else:
        form = QuestionForm(instance=question)
    context["form"] = form
    return render(request, "questions/question.html", context)

# Delete question
def delete_question(request, question_id):
    if not request.user.is_authenticated:
        messages.error(request, "Please Login to delete question.")
        return redirect("/")
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('/')

# Make private question to public
def make_public(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print("Send notification to staffs or admin(me) and provide public access")
    permission = True # Change it
    if permission:
        question.access = "Public"
        question.save()
    else:
        print("Send notif to user that it's not changed")
    return redirect(f'/questions/{question_id}')

# Make public questions to private
def make_private(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # Copying the tags of old to new object
    old_tags = question.tag.all()
    # Here, a new copy of  public question is taken and saved for that user.
    question.pk = None
    question.access = "Private"
    question.user = request.user
    question.save()
    question.tag.set(old_tags)
    messages.success(request, "A copy of the question is saved to your profile.")
    return redirect(f'/questions/{question.id}')

# Add a new tag
def add_tag(request):
    tag_name = request.GET.get('tag_name')
    tag_name = tag_name.capitalize()
    data = {}
    if tag_name == '' or Tag.objects.filter(name = tag_name).exists():
        data["present"] = True
        data["errorMessage"] = f"{tag_name} is already present in tag list.";
    else:
        data["present"] = False
        tag = Tag(name = tag_name)
        tag.save()
        data["value"] = Tag.objects.get(name = tag_name).pk
        data["text"] = tag_name
    return JsonResponse(data)

# View full details of the question and add and edit solution for that question.
def view_question(request, question_id, solution_id=None):
    if not request.user.is_authenticated:
        messages.error(request, "Please log in to view questions")
        return redirect("/")
    context = {}
    question = get_object_or_404(Question, pk=question_id)
    solutions = Solution.objects.filter(question = question).order_by('-date_added')
    if request.method == "POST":
        title           = request.POST.get('soln-title')
        if not title:
            title = "Solution " + str(len(solutions)+1)
        description     = request.POST.get('soln-desc')
        language        = request.POST.get('language')
        code            = request.POST.get('code')
        link            = request.POST.get('link')
        print(title,"Notes", description)
        print('Code', code, language)
        if solution_id:
            # Edit solution
            new_solution = get_object_or_404(Solution, pk=solution_id)
            new_solution.title = title
            new_solution.language = language
            new_solution.program = code
            new_solution.notes = description
            new_solution.link = link
        else:
            # Add solution
            new_solution = Solution(
                question    = question,
                title       = title, 
                language    = language,
                program     = code,
                notes       = description,
                link        = link
            )
        new_solution.save()
        solutions |= Solution.objects.filter(pk=new_solution.pk)
    context['question'] = question
    context['solutions'] = solutions    
    return render(request, "questions/display_question.html", context)

# Delete solution
def delete_solution(request, question_id, solution_id):
    if not request.user.is_authenticated:
        messages.error(request, "Please Login to delete solution.")
        return redirect("/")
    solution = get_object_or_404(Solution, pk=solution_id)
    solution.delete()
    return redirect(f"/questions/{question_id}")