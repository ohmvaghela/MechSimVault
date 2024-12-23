from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .manager import SiteUserManager
import os
from django.utils.deconstruct import deconstructible

@deconstructible
class PathAndRename:
    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = f'{instance.email}.{ext}'
        return os.path.join('profile_pictures/', filename)
path_and_rename = PathAndRename()


class SiteUser(AbstractBaseUser, PermissionsMixin):
  # profile picture
  profile_picture = models.ImageField(upload_to=path_and_rename, default='profile_picture/image.png', null=True, blank=True)  
  email = models.EmailField("email id", max_length=254, unique=True)
  is_superuser = models.BooleanField("is_superuser", default=False)
  full_name = models.CharField("full name", max_length=50, default="Default name")
  bio = models.CharField("bio", max_length=500, default="", blank=True)
  institution = models.CharField("institution", max_length=250, default="", blank=True)  # Corrected typo
  role = models.CharField("role", max_length=250, default="", blank=True)
  country = models.CharField("country", max_length=250, default="INDIA", blank=True)
  contact_info = models.CharField("contact info", max_length=250, default="", blank=True)
  skills = models.CharField("skills", max_length=250, default="", blank=True)
  signup_date = models.DateTimeField("user creation date", default=timezone.now)

  USERNAME_FIELD = "email"
  REQUIRED_FIELDS = []

  objects = SiteUserManager()

  def __str__(self):
    return self.email

