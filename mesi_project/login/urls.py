from django.urls import path
from . import views

urlpatterns = [
    path('signupSubmit/', views.signupSubmit, name='signupSubmit'),
    path('signup/', views.signup, name='signup'),
    path('', views.index, name='index'),
]
