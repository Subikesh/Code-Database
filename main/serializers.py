from rest_framework import serializers
from .models import Question, Tag, Solution

class QuestionSerializer(serializers.ModelSerializer):
    # Making user read-only field
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')    

    class Meta:
        model = Question
        fields = ['id', 'user', 'user_id', 'title', 'access', 'description', 'link', 'difficulty', 'tag', 'examples', 'date_added']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'description']

class SolutionSerializer(serializers.ModelSerializer):
    question_title = serializers.ReadOnlyField(source='question.title')

    class Meta:
        model = Solution
        fields = ['id', 'question_title', 'title', 'language', 'program', 'notes', 'link', 'date_added']