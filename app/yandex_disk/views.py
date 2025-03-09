import urllib
import requests


from django.contrib.auth import login
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm


YANDEX_DISK_API_BASE_URL = "https://cloud-api.yandex.net/v1/disk/public/resources"


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


@login_required
def list_files(request):

    public_key = request.GET.get('public_key', '')

    if not public_key:

        return JsonResponse({'error': 'Public key is required'}, status=400)

    params = {'public_key': public_key}
    response = requests.get(YANDEX_DISK_API_BASE_URL, params=params)

    if response.status_code == 200:

        data = response.json()
        return JsonResponse(data)

    else:

        return JsonResponse({'error': 'Failed to fetch files'}, status=response.status_code)


@login_required
def download_file(request):

    file_url: str = request.GET.get('file_url', '')

    if file_url:

        return redirect(file_url)
    
    else:

        return JsonResponse('file_url parameter is required')
