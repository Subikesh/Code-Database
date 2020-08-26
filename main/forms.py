from django import forms
from .models import Question, Solution

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ["title", "link", "description", "difficulty", "tag", "examples"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "link": forms.URLInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "difficulty": forms.Select(attrs={"class": "form-control"}),
            "tag": forms.Select(attrs={"class": "form-control"}),
            "examples": forms.Textarea(attrs={"class": "form-control"})
        }
        

