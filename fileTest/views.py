from django.http import JsonResponse
from django.conf import settings
import os

def list_files(request):
    media_path = os.path.join(settings.MEDIA_ROOT, 'profile_picture')
    files = os.listdir(media_path)
    return JsonResponse({'files': files})