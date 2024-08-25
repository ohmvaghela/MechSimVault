from django.db import models
from django.utils import timezone
import os
import shutil
from django.conf import settings

class Simulation(models.Model):
    user_id = models.ForeignKey("siteUser.SiteUser", verbose_name="Site User", on_delete=models.CASCADE)
    upload_date = models.DateField("upload data", default=timezone.now().date())
    # likes = models.IntegerField("likes", default=0)
    dislikes = models.IntegerField("dislikes", default=0)
    title = models.CharField("Simulation title", max_length=50, default="")
    description = models.CharField("Simulation title", max_length=250, default="")
    Softwares = models.CharField("Simulation title", max_length=50, default="")
    simulation_image = models.ImageField("Simulation disp image", upload_to="simulations/", default='simulations/default_photo.png')
    zip_file = models.FileField(upload_to="simulations/", verbose_name="Simulation Zip File", blank=True)
    zip_photos = models.FileField(upload_to="simulations/", verbose_name="Simulation Images", blank=True)

    def save(self, *args, **kwargs):
      if not self.pk:
        # self.likes = 0
        self.dislikes = 0
      super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
      self.delete_zip_file()
      self.delete_zip_photos()
      self.delete_simulation_image()
      super().delete(*args, **kwargs)

    def delete_zip_file(self):
        if self.zip_file and os.path.isfile(self.zip_file.path):
            os.remove(self.zip_file.path)
            self.zip_file = None
            self.save()

    def delete_zip_photos(self):
        if self.zip_photos and os.path.isfile(self.zip_photos.path):
            os.remove(self.zip_photos.path)
            self.zip_photos = None
            self.save()

    def delete_simulation_image(self):
        if self.simulation_image and os.path.isfile(self.simulation_image.path):
            os.remove(self.simulation_image.path)
            self.simulation_image = None
            self.save()

    def __str__(self):
        return f"Simulation by {self.user_id.email} : {self.title}"

  
class Likes(models.Model):
  user_id = models.ForeignKey("siteUser.SiteUser", verbose_name="site user", on_delete=models.CASCADE)
  sim_id = models.ForeignKey("simulations.Simulation", verbose_name="simuation id", on_delete=models.CASCADE)
  class Meta:
    unique_together = ('user_id', 'sim_id')

