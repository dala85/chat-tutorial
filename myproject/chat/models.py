from django.db import models


class Chat(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
