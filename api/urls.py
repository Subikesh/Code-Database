from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('questions/', views.QuestionList.as_view(), name="add_question"),
    path('questions/<int:pk>/', views.QuestionRetrieve.as_view(), name="view_question"),
    path('solutions/<int:question_id>/', views.SolutionList.as_view(), name="add_solution"),
    path('solutions/<int:question_id>/<int:pk>/', views.SolutionRetrieve.as_view(), name="view_solution"),
    path('tag/', views.CreateTag.as_view(), name="create_tag"),
    path('tag/<int:pk>/', views.DeleteTag.as_view(), name="view_tag"),
]
