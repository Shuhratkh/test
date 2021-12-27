from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Answer(models.Model):
    body=models.TextField()

    def __str__(self):
        return self.body

class Question(models.Model):
    body=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    answer=models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.body
    def get_absolute_url(self):
        return reverse('home')


class Survey(models.Model):
    question=models.OneToOneField(Question, on_delete=models.CASCADE)
    title=models.CharField(max_length=75)
    date_created=models.DateField()
    date_ended=models.DateField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('home')