from django.urls import path
from . import views
from .views import HeroStoryListView

app_name = "board"

urlpatterns = [
    path('story/', views.hero_story, name='story'),
    path('test', views.index, name='index'),
    path('', HeroStoryListView.as_view(), name='herostory-list')
]
