from siteUser.models import SiteUser

users = SiteUser.objects.all()
for user in users:
  print(user.id)
  print(user.email)
  print(user.password)
  print(user.full_name)
  print(user.bio)
  print(user.institution)
  print(user.role)
  print(user.country)
  print(user.contact_info)
  print(user.skills)  
  print(f'-'*20)