from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    contact = models.CharField(max_length=13)
    
    user_type = models.CharField(max_length=1,choices = (
        ('E',"Employeer"),
        ('J',"Job-Seeker"),
    ))
    def __str__(self):
        return self.username
