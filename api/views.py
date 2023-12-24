from django.shortcuts import render
from main.models import Question, Solution, Tag
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from .serializers import QuestionSerializer, SolutionSerializer, TagSerializer


# Custom permission to check if the question's owner is trying to update the question
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allows GET, HEAD or OPTIONS requests
        if request.method in permissions.SAFE_METHODS:
            return True
        # If current user is the object user
        return obj.user == request.user


# List all the public questions and user-private questions
class QuestionList(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # If user views anonymously, public questions are shown
        query = Question.objects.filter(access="Public")
        # User authenticated can see his questions and all public questions
        if self.request.user.is_authenticated:
            query = query | Question.objects.filter(user=self.request.user)
        return query

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Retrieve, Update and delete a question from given pk
class QuestionRetrieve(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly & IsOwnerOrReadOnly]

    def get_queryset(self):
        # If user views anonymously, public questions are shown
        query = Question.objects.filter(pk=self.kwargs.get('pk'))
        if query.filter(access="Public").exists() or (
                self.request.user.is_authenticated and query.filter(user=self.request.user).exists()):
            return query
        else:
            return None


# Create a new tag from API call with ../api/tag/
class CreateTag(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        # if not serializer.is_valid():
        #     raise ValidationError(f"The new tag {serializer.validated_data['name']} already exists")
        if serializer.is_valid():
            serializer.save()


# Delete a tag from pk as url
class DeleteTag(generics.RetrieveDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAdminUser]


# List all the solutions for a question and create new solution
class SolutionList(generics.ListCreateAPIView):
    serializer_class = SolutionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        question = Question.objects.get(pk=self.kwargs.get('question_id'))
        print(question)
        return Solution.objects.filter(question=question)

    def perform_create(self, serializer):
        question = Question.objects.get(pk=self.kwargs.get('question_id'))
        if question.user != self.request.user:
            raise ValidationError("Check the question id in url")
        serializer.save(question=question)


# Retrieve a specific solution and update or delete it
class SolutionRetrieve(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SolutionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly & IsOwnerOrReadOnly]

    def get_queryset(self):
        question = Question.objects.get(pk=self.kwargs.get('question_id'))
        print(question)
        return Solution.objects.filter(question=question)
