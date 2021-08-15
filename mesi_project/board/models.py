from django.db import models
from django.contrib.auth import get_user_model


class HeroStory(models.Model):
    text = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
