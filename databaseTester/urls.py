from django.urls import path
from . import views

urlpatterns = [
  path("showUsers/", views.showUsers, name="all_users")
]
