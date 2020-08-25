from django.db import models
from django.conf import settings

# Create your models here.
class Question(models.Model):
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="User", on_delete = models.CASCADE)
    title           = models.CharField(max_length = 200)
    description     = models.TextField(null = True)
    link            = models.URLField(null = True)
    difficulty      = models.TextField(max_length = 10)
    Other           = models.TextField(null = True)

    def __str__(self):
        return self.title

class Solution(models.Model):
    question        = models.ForeignKey(Question, verbose_name="Question", on_delete = models.CASCADE)
    title           = models.CharField(max_length = 100)
    language        = models.CharField(max_length = 20)
    program         = models.TextField(null = True)
    notes           = models.TextField(null = True)
    link            = models.URLField(null = True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    question        = models.ManyToManyField(Question)
    name            = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
