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
    path('add_question', views.add_question, name="add_question"),
    path('add_question/<int:question_id>', views.add_question, name="edit_question"),
    path('add_tag', views.add_tag, name="add_question_tag"),
    path('questions/<int:question_id>/', views.view_question, name="view_question"),
    path('questions/<int:question_id>/<int:solution_id>/', views.view_question, name="edit_solution"),
]
