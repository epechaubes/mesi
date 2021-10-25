from django.conf import settings
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import HeroStoryListView

app_name = "board"

urlpatterns = [
    path('story/', views.hero_story, name='story'),
    path('', views.index, name='index'),
    path('list', HeroStoryListView.as_view(), name='herostory-list')
]
