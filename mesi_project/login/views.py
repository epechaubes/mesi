from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import SignUpForm
import logging


logger = logging.getLogger(__name__)
template = 'login/signup.html'

def index(request):
    return HttpResponse("Index page")
