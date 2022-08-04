import django.contrib.auth.models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import ForeignKey


class Todo(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)