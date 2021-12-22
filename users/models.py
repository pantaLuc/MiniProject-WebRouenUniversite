from __future__ import annotations
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models.deletion import CASCADE

class User(AbstractUser):
    ROLES = [
        ('admin', 'admin'),
        ('responsable', 'responsable'),
    ]
    
    username=models.CharField(max_length=10 , unique=True)
  
    role = models.CharField(
        max_length=13,
        choices=ROLES,
        null=True, 
        blank=True,
        default="responsable"
        )
    USERNAME_FIELD = 'username'
    objects=UserManager()
    def __str__(self):
        return self.username