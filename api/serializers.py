from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from main.models import Question, Tag, Solution

class SolutionSerializer(serializers.ModelSerializer):
    question_title = serializers.ReadOnlyField(source='question.title')

    class Meta:
        model = Solution
        fields = ['id', 'question_title', 'title', 'language', 'program', 'notes', 'link', 'date_added']

class QuestionSerializer(serializers.ModelSerializer):
    # Making user read-only field
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')    
    solutions = SolutionSerializer(many=True, read_only=True)
    solution_count = serializers.ReadOnlyField(source='solutions.count')

    class Meta:
        model = Question
        fields = ['id', 'user', 'user_id', 'title', 'access', 'description', 'link', 'difficulty', 'tag', 'examples', 'solution_count', 'solutions', 'date_added']

class TagSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, validators=[UniqueValidator(queryset=Tag.objects.all())])
    questions_count = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ['id', 'name', 'description',  'questions_count']
    
    def get_questions_count(self, tag):
        return tag.questions.count()
