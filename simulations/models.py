from django.db import models
from django.utils import timezone
class Simulation(models.Model):
  user_id = models.ForeignKey("siteUser.SiteUser", verbose_name="Site User", on_delete=models.CASCADE)
  upload_date = models.DateField("upload data", default=timezone.now)
  likes = models.IntegerField("likes",default=0)
  dislikes = models.IntegerField("dislikes",default=0)
  title = models.CharField("Simulation title", max_length=50,default="")
  description = models.CharField("Simulation title", max_length=250,default="")
  Softwares = models.CharField("Simulation title", max_length=50,default="")
  zip_file = models.FileField(upload_to='simulations/zips/', verbose_name="Simulation Zip File")
  
  def save(self,*args, **kawrgs):
    if not self.pk:
      self.likes = 0
      self.dislikes = 0
    super().save(*args,**kawrgs)
      
  def __str__(self):
    return f"Simulation by {self.user_id.email} : {self.title}"
  
class SimulationPhoto(models.Model):
    simulation = models.ForeignKey(Simulation, related_name='photos', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='simulations/photos/', verbose_name="Simulation Photo")
    
    def __str__(self):
        return f"Photo for {self.simulation.title}"