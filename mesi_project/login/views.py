from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse

from .forms import SignUpForm
import logging


logger = logging.getLogger(__name__)
signUpTemplate = 'login/signup.html'
loginTemplate = 'login/index.html'
boardTemplate = 'board/index.html'


def index(request):
    if not request.method == 'POST':
        return render(request, loginTemplate)

    email = request.POST.get('email', False)
    password = request.POST.get('password', False)

    user = authenticate(request, email=email, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("board:herostory-list"))
    else:
        messages.add_message(
            request, messages.ERROR, "Les champs renseignés sont invalides."
        )
        return redirect("login:index")


def signup(request):
    if not request.method == 'POST':
        form = SignUpForm()
        context = {'form': form}
        return render(request, signUpTemplate, context)

    form = SignUpForm(request.POST)

    if not form.is_valid():
        return render(request, signUpTemplate, {'form': form})

    form.save()
    return redirect('login:index')
