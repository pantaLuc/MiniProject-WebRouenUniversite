
#from ressources.models import Service
from django.utils import timezone
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import PermissionsMixin



# Create your models here.
class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(('The given username must be set'))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, password=username ,role='responsable',
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False, ' ',
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True,
                                 **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user






class User(AbstractBaseUser, PermissionsMixin):
    ROLES = [
        ('admin', 'admin'),
        ('responsable', 'responsable'),
    ]
    
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=250, unique=True)
    prenom = models.CharField(max_length=30, blank=True, null=True)
    nom = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    role = models.CharField(
        max_length=13,
        choices=ROLES,
        null=True, 
        blank=True,
        default="responsable"
        # Roles, on_delete=models.CASCADE, related_name='role_user', null=True, blank=True
        )
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]