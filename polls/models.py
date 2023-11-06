from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.question

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
