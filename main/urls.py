from django.urls import path, include
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('register', views.register, name="register"),
    path('login', views.homepage, name="login"),
    path('logout', views.logout, name="logout"),
    path('profile', views.profile, name="profile"),
    path('delete', views.delete, name="delete"),

    path('add_tag', views.add_tag, name="add_question_tag"),
    path('add_question', views.add_question, name="add_question"),
    path('add_question/<int:question_id>', views.add_question, name="edit_question"),
    path('delete_question/<int:question_id>/', views.delete_question, name="delete_question"),
    path('make_public/<int:question_id>', views.make_public, name='make_public'),
    path('make_private/<int:question_id>', views.make_private, name='make_private'),

    path('questions/<int:question_id>/', views.view_question, name="view_question"),
    path('questions/<int:question_id>/<int:solution_id>/', views.view_question, name="edit_solution"),
    path('delete_solution/<int:question_id>/<int:solution_id>', views.delete_solution, name="delete_solution")
]
