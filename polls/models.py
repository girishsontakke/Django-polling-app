from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth import get_user_model
import datetime

User = get_user_model()

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200, null=False)
    pub_date = models.DateTimeField(default=timezone.now)

    def was_published_recently(self):
        now = timezone.now()
        return now >= self.pub_date >= now-datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse("polls:index")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.ManyToManyField(User)

    def __str__(self):
        return self.choice_text
