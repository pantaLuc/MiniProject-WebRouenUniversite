from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import  AnomalieRessource, Ressource , Localisation ,Service,Anomalie


class RessourceSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id' , 'nomRessource' , 'descriptionRes' , 'localisation' , 'responsable' ,'service')
        model=Ressource

class ServiceSerializer(serializers.ModelSerializer):
    class Meta :
        fields=('id' ,'nomServ' , 'descriptionService', 'creer_le' ,'responsables')
        model=Service
class AnomalieSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id' ,'nomAnomalie','descriptionAnomalie')
        model=Anomalie
class LocalisationSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id' , 'code' ,'libelle' ,'description')
        model=Localisation  
           
class AnomalieRessourceSerializers(serializers.ModelSerializer):
    class Meta:
        fields=('id','localisation' ,'ressource','anomalie' ,'detecter_le','corriger_le', 'etat','nombreSignalement')
        model=AnomalieRessource