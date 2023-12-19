from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default="John Smith")
    title = models.CharField(max_length=30, default="default")
    location = models.CharField(max_length=30, default="default")
    message = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now())