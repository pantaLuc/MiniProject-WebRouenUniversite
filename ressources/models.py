#from users.models import User
from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.

#creation des models pour ressources 

class Localisation(models.Model):
    code = models.CharField(max_length=10, unique = True)
    libelle = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    def __str__(self):
        return self.code

class Anomalie(models.Model):
    nomAnomalie=models.CharField(max_length=100) 
    descriptionAnomalie=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nomAnomalie

class Service(models.Model):
    nomServ=models.CharField(max_length=50)
    descriptionService=models.CharField(max_length=200)

    def __str__(self):
        return self.nomServ

class Ressource(models.Model):
    #user=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    nomRessource=models.CharField(max_length=50)
    descriptionRes=models.CharField(max_length=200)
    localisation=models.ForeignKey(Localisation ,on_delete=models.CASCADE)
    creer_le=models.DateTimeField(auto_now_add=True)
    modifier_le=models.DateTimeField(auto_now_add=True)
    services=models.ForeignKey(Service,on_delete= models.CASCADE ,null=True)
    
    def __str__(self):
        return self.nomRessource

class AnomalieRessource(models.Model):
    ressource=models.ForeignKey(Ressource ,on_delete=models.CASCADE)
    anomalie=models.ForeignKey(Anomalie , on_delete=models.CASCADE)
    est_present=models.BooleanField(null=False)
    localisation=models.ForeignKey(Localisation ,on_delete=models.CASCADE)
    detecter_le=models.DateTimeField(auto_now_add=True)
    corriger_le=models.DateTimeField(auto_now_add=True)
    
    