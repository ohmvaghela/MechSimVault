from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _ 

class SiteUserManager(BaseUserManager):
  
  # create user using email
  def create_user(self,email,password,**extra_fields):
    
    if not email:
      raise ValueError("Email not present")
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    # create hashed password
    user.set_password(password)
    user.save()
    return user
  
  def create_superuser(self, email, password, **extra_fields):
    extra_fields.setdefault("is_superuser", True)
    return self.create_user(email,password,**extra_fields)