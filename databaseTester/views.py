from django.shortcuts import render
from siteUser.models import SiteUser

def showUsers(request):
  users = SiteUser.objects.all()
  return render(request,'showusers.html',{'users':users})

