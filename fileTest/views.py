from django.http import JsonResponse
from django.conf import settings
import os

def list_files(request):
    media_path = os.path.join(settings.MEDIA_ROOT, 'profile_picture')
    files = os.listdir(media_path)
    return JsonResponse({'files': files})


def check_file_permissions(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'profile_picture', 'base.jpg')
    if os.path.exists(file_path):
        permissions = oct(os.stat(file_path).st_mode)[-3:]
        return JsonResponse({'file_exists': True, 'permissions': permissions})
    else:
        return JsonResponse({'file_exists': False, 'permissions': None})