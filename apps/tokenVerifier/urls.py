from django.urls import path
from . import views
urlpatterns = [
  path("token_verify/",views.VerifyAndRefreshTokenView.as_view(),name="token-verifier"),
]
