import os
import io
import requests
import zipfile
import json

from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse

from django.shortcuts import redirect, render

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from django.core.cache import cache

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

    if data := cache.get(public_key):
        
        print('cached data return', os.getenv('REDIS_URL'))
        return JsonResponse(data)
    
    else:

        response = requests.get(YANDEX_DISK_API_BASE_URL, params=params)

        if response.status_code == 200:

            data = response.json()
            cache.set(key=public_key, value=data, timeout=int(os.getenv('FOLDER_CACHE_SECONDS')))

            return JsonResponse(data)

        else:

            return JsonResponse({'error': 'Failed to fetch files'}, status=response.status_code)


@login_required
def download_file(request):

    if request.method == 'GET':

        file_url: str = request.GET.get('file_url', '')
        
        if file_url:

            return redirect(file_url)
        
        else:

            return JsonResponse('file_url parameter is required')
        
        
    # TODO лучше сделать временный зип(он хавает время ответа из-за ожидания закрытия fileresponse), а не хранить в памяти, генерить с u_id
    elif request.method == 'POST':

        try:
            files = json.loads(request.POST.get('files', '[]'))  # ✅ Получаем список словарей [{file_url, file_name}]
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

        if not files:
            return JsonResponse({'error': 'No files selected'}, status=400)

        # буффер для зипа
        zip_buffer = io.BytesIO() 

        with zipfile.ZipFile(zip_buffer, 'w') as zip_file:

            for file in files:
            
                file_url = file.get("file_url")
                file_name = file.get("file_name")

                if not file_url or not file_name:
                    continue  

                response = requests.get(file_url, stream=True)

                if response.status_code == 200:
                    zip_file.writestr(file_name, response.content)


        # буффер для зипа
        zip_buffer.seek(0)  

        response = HttpResponse(zip_buffer, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="selected_files.zip"'

        return response
