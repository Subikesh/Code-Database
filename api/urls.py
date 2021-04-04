from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('questions/', views.QuestionList.as_view()),
    path('questions/<int:pk>/', views.QuestionRetrieve.as_view()),
    path('solutions/<int:question_id>/', views.SolutionList.as_view()),
    path('solutions/<int:question_id>/<int:pk>/', views.SolutionRetrieve.as_view()),
    path('tag/', views.CreateTag.as_view()),
    path('tag/<int:pk>/', views.DeleteTag.as_view()),
]
