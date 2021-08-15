from django.conf import settings
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = "board"

urlpatterns = [
    path('story/', views.hero_story, name='story'),
    path('', views.index, name='index'),
]