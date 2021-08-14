from django.urls import path
from . import views


app_name = "board"

urlpatterns = [
    # path('logout/', views.logout, name='logout'),
    path('', views.index, name='index'),
]