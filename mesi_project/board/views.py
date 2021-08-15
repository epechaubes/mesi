import logging

from django.forms import ModelForm
from django.shortcuts import render, redirect
from .models import HeroStory

logger = logging.getLogger(__name__)
newHeroStoryTemplate = 'board/newHeroStory.html'


class HeroStoryForm(ModelForm):
    class Meta:
        model = HeroStory
        fields = ('text', )


def index(request):
    return render(request, 'board/index.html')
