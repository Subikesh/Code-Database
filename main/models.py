from django.db import models
from django.conf import settings

class Tag(models.Model):
    name            = models.CharField(max_length = 100, unique= True)
    description     = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Question(models.Model):
    difficulty_choices = [
        ("Hard", "Hard"),
        ("Medium", "Medium"),
        ("Easy", "Easy"),
    ]
    access_choices = [
        ("Private", "Private"),
        ("Public", "Public")
    ]
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="User", on_delete = models.CASCADE, related_name='questions')
    title           = models.CharField(max_length = 200)
    access          = models.CharField(max_length = 10, choices = access_choices, default = "Private")
    description     = models.TextField(null = True, blank = True)
    link            = models.URLField(null = True, blank = True)
    difficulty      = models.TextField(max_length = 10, choices = difficulty_choices)
    tag             = models.ManyToManyField(Tag, related_name='questions', blank=True)
    examples        = models.TextField(null = True, blank = True)
    date_added      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Solution(models.Model):
    access_choices = [
        ("Private", "Private"),
        ("Public", "Public")
    ]
    question        = models.ForeignKey(Question, verbose_name="Question", on_delete = models.CASCADE, related_name='solutions')
    title           = models.CharField(max_length = 100)
    access          = models.CharField(max_length = 10, choices = access_choices, default = "Private")
    language        = models.CharField(max_length = 20)
    program         = models.TextField(null = True, blank = True)
    notes           = models.TextField(null = True, blank = True)
    link            = models.URLField(null = True, blank = True)
    date_added      = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['question', '-date_added']

    def __str__(self):
        return self.title
