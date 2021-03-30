from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer):
    # Making user not read-only
    user = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')    

    class Meta:
        model = Question
        fields = ['id', 'user', 'user_id', 'title', 'access', 'description', 'link', 'difficulty', 'tag', 'examples', 'date_added']