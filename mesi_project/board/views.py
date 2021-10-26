import logging

from django.contrib.auth.models import Group
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import TemplateView

from .models import HeroStory

logger = logging.getLogger(__name__)
newHeroStoryTemplate = 'board/newHeroStory.html'


class HeroStoryForm(ModelForm):
    class Meta:
        model = HeroStory
        fields = ('text', )


class HeroStoryListView(generic.ListView):
    model = HeroStory
    context_object_name = 'herostory_list'
    paginate_by = 6


def index(request):
    return render(request, 'board/index.html')


def hero_story(request):
    if not request.method == 'POST':
        form = HeroStoryForm()
        context = {'form': form}
        return render(request, newHeroStoryTemplate, context)

    form = HeroStoryForm(request.POST)
    if not form.is_valid():
        logger.error("Not valid")
        return render(request, newHeroStoryTemplate, {'form': form})

    obj = form.save(commit=False)
    obj.author = request.user
    obj.save()
    return redirect('board:index')

