from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class App(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)  # Link profile to user
    app_name=models.CharField(max_length=100)
    app_points=models.IntegerField(default=0)
    app_link=models.URLField()
    app_image=models.ImageField(upload_to='app_images/', blank=True, null=True)
    app_category=models.CharField( max_length=50, blank=True, null=True)
    app_types=models.CharField( max_length=50, blank=True, null=True)
    user_points=models.IntegerField(default=0)

    def __str__(self):
      return self.app_name
    

    
class Doc(models.Model):
   upload = models.ImageField(upload_to='images/')

   def __str__(self):
      return str(self.pk)
   


        
    



