from __future__ import annotations
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models.deletion import CASCADE
from ressources.models  import Ressource, Service 

   
class User(AbstractUser):
    ROLES = [
        ('admin', 'admin'),
        ('responsable', 'responsable'),
    ]
    
    username=models.CharField(max_length=10 , unique=True)
    service=models.ForeignKey(Ressource , on_delete=models.CASCADE, null=True)
    role = models.CharField(
        max_length=13,
        choices=ROLES,
        null=True, 
        blank=True,
        default="responsable"
        # Roles, on_delete=models.CASCADE, related_name='role_user', null=True, blank=True
        )
    USERNAME_FIELD = 'username'
    objects=UserManager()
    def __str__(self):
        return self.username