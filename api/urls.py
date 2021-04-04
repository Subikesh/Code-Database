from django.urls import path, include
from . import views

app_name = 'main'
urlpatterns = [
    # path('api/questions/', views.QuestionList.as_view(), name="api_questions"),
    # path('api/questions/<int:pk>/', views.QuestionRetrieve.as_view(), name="api_view_question"),
    # path('api/solutions/<int:question_id>/', views.SolutionList.as_view(), name="api_solution"),
    # path('api/solutions/<int:question_id>/<int:pk>/', views.SolutionRetrieve.as_view(), name="api_solution_update"),
    # path('api/tag/', views.CreateTag.as_view(), name="api_create_tag"),
    # path('api/tag/<int:pk>/', views.DeleteTag.as_view(), name="api_delete_tag"),
]
