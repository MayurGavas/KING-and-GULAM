from django.db import models

# Create your models here.
class UserProfile(models.Model):
    profile_pic = models.CharField(max_length=255, blank = True)