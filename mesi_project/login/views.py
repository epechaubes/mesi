from django.contrib.auth import authenticate, login, logout
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

def logout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, "Vous êtes déconnecté !")
    return redirect("index")

def index(request):
    if not request.method == 'POST':
        return render(request, loginTemplate)

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)

    user = authenticate(request, username=username, password=password)
    logger.error(user)

    if user is not None:
        login(request, user)
        testUser = request.user.is_authenticated
        # return render(request, boardTemplate)
        # redirect("boardi")
        return HttpResponseRedirect(reverse("board:index"))
    else:
        messages.add_message(
            request, messages.ERROR, "Les champs renseignés sont invalides."
        )
        logger.error(messages)
        return redirect("index")



def signup(request):
    if not request.method == 'POST':
        form = SignUpForm()
        context = {'form': form}
        return render(request, signUpTemplate, context)

    form = SignUpForm(request.POST)

    if not form.is_valid():
        return render(request, signUpTemplate, {'form': form})

    form.save()
    return redirect('index')