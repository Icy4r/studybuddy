from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default="No Name")
    bio = models.CharField(max_length=3000, default="")
    classes = models.CharField(max_length=3000, default="")