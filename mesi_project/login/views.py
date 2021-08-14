from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import SignUpForm
import logging


logger = logging.getLogger(__name__)
template = 'login/signup.html'

def index(request):
    return HttpResponse("Index page")

def signup(request):
    return render(request, template)

def signupSubmit(request):
    if not request.method == 'POST':
        form = SignUpForm()
        context = {'form': form}
        return render(request, template, context)

    form = SignUpForm(request.POST)

    if not form.is_valid():
        return render(request, template)

    form.save()
    return redirect('index')