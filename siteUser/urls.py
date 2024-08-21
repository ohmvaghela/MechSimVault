from django.urls import path
from . import views

urlpatterns = [
  path("get_users/",views.SiteUserList.as_view(),name="list-site-user"),
  path("create_user/",views.SiteUserCreate.as_view(),name="create-user"),
  path("login_user/",views.SiteUserLogin.as_view(),name="user-login"),
  path('update/', views.SiteUpdateUser.as_view(), name='user-update'),
  path('update_password/', views.SiteUpdatePassword.as_view(), name='user-update-password'),

]
