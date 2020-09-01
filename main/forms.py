from django import forms
from .models import Question, Solution

class QuestionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(QuestionForm, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Question
        fields = ["title", "link", "description", "difficulty", "tag", "examples"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "link": forms.URLInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "difficulty": forms.Select(attrs={"class": "form-control"}),
            "tag": forms.SelectMultiple(attrs={"class": "form-control"}),
            "examples": forms.Textarea(attrs={"class": "form-control"})
        }
        
    def clean_title(self):
        title = self.cleaned_data.get("title")
        if self.instance.pk == None:
            if Question.objects.filter(title=title).filter(user=self.user).exists():
                raise forms.ValidationError("The question '%s' already exists" %(title))
        return title