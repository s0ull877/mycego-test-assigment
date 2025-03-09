from django.urls import path
from .views import index, signup, list_files, download_file

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('list/', list_files, name='list_files'),
    path('download/', download_file, name='download_file'),
]