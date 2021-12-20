from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from ressources.models import Service 
class User(AbstractUser):
    ROLES = [
        ('admin', 'admin'),
        ('responsable', 'responsable'),
    ]
    
    username=models.CharField(max_length=10 , unique=True)
    service=models.ForeignKey(Service , on_delete=models.CASCADE ,null=True)
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