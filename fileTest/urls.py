from django.urls import path
from .views import list_files,check_file_permissions

urlpatterns = [
    # ... your other url patterns
    path('list-files/', list_files, name='list_files'),
    path('check-permissions/', check_file_permissions, name='check_permissions'),
]
