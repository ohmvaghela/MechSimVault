from django.urls import path
from .views import list_files

urlpatterns = [
    # ... your other url patterns
    path('list-files/', list_files, name='list_files'),
]
