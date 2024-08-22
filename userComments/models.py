from django.db import models
from django.utils import timezone

class Comments(models.Model):
  user = models.ForeignKey("siteUser.SiteUser", verbose_name="Site User", on_delete=models.CASCADE)
  simulation = models.ForeignKey("simulations.Simulation", verbose_name="simulation_id", on_delete=models.CASCADE)
  date = models.DateTimeField("comment date", default=timezone.now)
  likes = models.IntegerField("likes", default=0)# user cannot add this
  message = models.CharField("user messaeg", max_length=500)
  
  def save(self, *args, **kwargs):
    if not self.pk:
        self.likes = 0
    super().save(*args, **kwargs)
  
  def __str__(self):
    return f"Comment on {self.simulation.title} on {self.user.email}" 
  
  