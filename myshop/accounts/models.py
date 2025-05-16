from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):
    phone=models.CharField(max_length=20)
    street_address=models.CharField(max_length=200)


