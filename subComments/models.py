from django.db import models
from django.utils import timezone
class SubComments(models.Model):
  comment_id = models.ForeignKey("userComments.Comments", verbose_name="Comments", on_delete=models.CASCADE)
  user_id = models.ForeignKey("siteUser.SiteUser", verbose_name="User", on_delete=models.CASCADE)
  message = models.CharField("message", max_length=500)
  date = models.DateTimeField("creation date",default=timezone.now)
  likes = models.IntegerField("likes",default=0)
  
  def save(self, *args, **kwags):
    if not self.pk:
      self.likes = 0
    super().save(*args,**kwags)
  
  def __str__(self):
    return f"Comment by {self.user_id.email} on {self.comment_id} at {self.date}"      
  
  