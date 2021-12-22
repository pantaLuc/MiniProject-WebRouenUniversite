from django.db.models import query
from django.http import response
from django.shortcuts import render
from rest_framework import generics, serializers ,viewsets,permissions
from rest_framework.decorators import permission_classes

from ressources.serializers import AnomalieRessourceSerializers, AnomalieSerializer, LocalisationSerializer, RessourceSerializer, ServiceSerializer
from users.models import User
from users.serializers import UserSerializer
from .models import Anomalie, AnomalieRessource, Localisation, Ressource, Service
from rest_framework.response import Response

# Create your views here.

class CreerRessource(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated)
    queryset=Ressource.objects.all()
    serializer_class=RessourceSerializer

class RUDRessource(generics.RetrieveUpdateDestroyAPIView):
    queryset=Ressource.objects.all()
    serializer_class=RessourceSerializer

class CreerAnomalie(generics.CreateAPIView):
    queryset=Anomalie.objects.all()
    serializer_class=AnomalieSerializer
class RUDAnomalie(generics.RetrieveUpdateDestroyAPIView):
    queryset=Anomalie.objects.all()
    serializer_class=AnomalieSerializer

class CreerService(generics.CreateAPIView):
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer

class RUDService(generics.RetrieveUpdateDestroyAPIView):
    queryset=Service.objects.all()
    serializer_class=ServiceSerializer

class CreerLocalisation(generics.CreateAPIView):
    queryset=Localisation.objects.all()
    serializer_class=LocalisationSerializer

class RUDLocalisation(generics.RetrieveUpdateDestroyAPIView):
    queryset=Localisation.objects.all()
    serializer_class=LocalisationSerializer

class SignalerAnomalie(generics.CreateAPIView):
    queryset=AnomalieRessource.objects.all()
    serializer_class=AnomalieRessourceSerializers
    

class GestResponsable(viewsets.ViewSet):
    def ressourceResponsable(self , request , pk):
        #serializer =UserSerializer(request.user)
        #if serializer.data['role']=='responsable':
        queryset=Ressource.objects.filter(user=pk).all()
        serializer=RessourceSerializer(queryset,many=True)
        return Response(serializer.data)
    '''return Response({
            "message":"Vous n'etes pas autoriser a voir ces ressources"
        })'''
    def anomalieRessource(self ,request ,pk):
        queryset=AnomalieRessource.objects.filter(ressource=pk)
        serializers=AnomalieRessourceSerializers(queryset ,many=True)
        return Response(serializers.data)
class AdminGestion(viewsets.ViewSet):
     
     def listServices(self ,request):
        serializer = UserSerializer(request.user)
        if serializer.data['role']=='admin':
            queryset=Service.objects.all()
            serializer=ServiceSerializer(queryset ,many=True)
            return Response(serializer.data)
        return Response({
            "message":"Vous ne pouvez pas voir tout les services "
        })
     def listUserServices(self , request):
        serializers=UserSerializer(request.user)
        if serializers.data['role']=='admin':
            pass
   