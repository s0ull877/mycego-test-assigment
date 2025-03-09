from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms import SignUpForm


def index(request)  -> HttpResponse:

    return render(request=request, template_name='yandex_disk/index.html')


def signup(request) -> HttpResponseRedirect | HttpResponse:

    if request.method == "POST":
    
        form = SignUpForm(request.POST)
    
        if form.is_valid():
    
            user = form.save()
            login(request, user)
            return redirect('/')
    
    else:
    
        form = SignUpForm()
    
    return render(request, 'yandex_disk/signup.html', {'form': form})