from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Address(models.Model):
    Name= models.CharField(max_length=100)
    Email= models.EmailField(max_length=50,null=True)
    Address= models.CharField(max_length=100)
    Mobile= models.IntegerField(max_length=10)
    State= models.CharField(max_length=50)
    City= models.CharField(max_length=50,null=True)
    Pin= models.IntegerField(max_length=6)
    Landmark= models.CharField(max_length=100,null=True)
    