
from django.db import models
from django.db.models.deletion import CASCADE

#creation des models pour ressources 

class Localisation(models.Model):
    code = models.CharField(max_length=10, unique = True)
    libelle = models.CharField(max_length=255)
    description= models.CharField(max_length=255)
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
    creer_le=models.DateTimeField(auto_now_add=True)
    responsables=models.ManyToManyField('users.User')
    
    def __str__(self):
        return self.nomServ

class Ressource(models.Model):
    responsable=models.ForeignKey('users.User',on_delete=models.CASCADE)
    nomRessource=models.CharField(max_length=50)
    descriptionRes=models.CharField(max_length=200)
    localisation=models.ForeignKey(Localisation ,on_delete=models.CASCADE)
    creer_le=models.DateTimeField(auto_now_add=True)
    modifier_le=models.DateTimeField(auto_now_add=True)
    service=models.ForeignKey(Service,on_delete= models.CASCADE ,null=True)
    
    def __str__(self):
        return self.nomRessource

class AnomalieRessource(models.Model):
    ETAT = [
        ('present', 'present'),
        ('En cours de traitement', 'En cours de traitement'),
        ('terminé' , 'terminé')
    ]
    ressource=models.ForeignKey(Ressource ,on_delete=models.CASCADE)
    anomalie=models.ForeignKey(Anomalie , on_delete=models.CASCADE)
    etat = models.CharField(
        max_length=30,
        choices=ETAT,
        null=False, 
        blank=True,
        default="present"
        )
    nombreSignalement=models.IntegerField(default=0)
    localisation=models.ForeignKey(Localisation ,on_delete=models.CASCADE)
    detecter_le=models.DateTimeField(auto_now_add=True)
    corriger_le=models.DateTimeField(auto_now_add=True)
    
