from django.db.models import query
from django.http import response
from django.shortcuts import render
from rest_framework import generics, serializers ,viewsets,permissions
from rest_framework.decorators import api_view, permission_classes

from ressources.serializers import AnomalieRessourceSerializers, AnomalieSerializer, LocalisationSerializer, RessourceSerializer, ServiceSerializer
from users.models import User
from users.serializers import UserSerializer
from .models import Anomalie, AnomalieRessource, Localisation, Ressource, Service
from rest_framework.response import Response

# Create your views here.

class CreerRessource(generics.CreateAPIView):
    queryset=Ressource.objects.all()
    serializer_class=RessourceSerializer


    
class RUDRessource(generics.RetrieveUpdateDestroyAPIView):
    queryset=Ressource.objects.all()
    serializer_class=RessourceSerializer
class ListRessource(viewsets.ViewSet):
    def get(self ,request):
        queryset=Ressource.objects.all()
        serializer=RessourceSerializer(queryset ,many=True)
        return Response(serializer.data)
        LesUsers=querySet.responsables.all()
class ListUserParService(viewsets.ViewSet):
    def get(self ,request ,pk=None):
        querySet=Service.objects.get(id=pk)
        LesUsers=querySet.responsables.all()
        serializer=ServiceSerializer(querySet)
        return Response(serializer.data['responsables'])

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
class ListLocalisation(generics.ListAPIView):
    queryset=Localisation.objects.all()
    serializer_class=LocalisationSerializer

class SignalerAnomalie(generics.CreateAPIView):
    query=AnomalieRessource.objects.all()
    serializer_class=AnomalieRessourceSerializers

class ListAnomalieSignalerParRessource(viewsets.ViewSet):
    def get(self , request , pk):
        querySet=AnomalieRessource.objects.filter(ressource=pk).all()
        if querySet.exists():
            serializer=AnomalieRessourceSerializers(querySet,many=True)
            return Response(serializer.data)
        return Response({
            "message":"pas d' anomalie signaler pour cette Localisation"
        })


class SignalerAnomalieExistante(viewsets.ViewSet):
    def update(self ,request , pk=None):
        anomalieRessource=AnomalieRessource.objects.get(id=pk)
        serializer=AnomalieRessourceSerializers(instance=anomalieRessource ,data=request.data ,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class ListAnomalies(viewsets.ViewSet):
    def get (self , request):
        queryset=Anomalie.objects.all()
        if queryset.exists():
            serializer=AnomalieSerializer(queryset,many=True)
            return Response(serializer.data)
        return Response({
            "message":"pas d' anomalies"
        })
    
class RessourceLocalisation(viewsets.ViewSet):
    def get(self ,request ,pk):
        queryset=Ressource.objects.filter(localisation=pk).all()
        if queryset.exists():
            serializer=RessourceSerializer(queryset,many=True)
            return Response(serializer.data)
        return Response({
            "message":"cette Localisation n' a pas de resoource ou n' existe pas"
        })


            

class GestResponsable(viewsets.ViewSet):
    def ressourceResponsable(self , request , pk):
        #serializer =UserSerializer(request.user)
        #if serializer.data['role']=='responsable':
        queryset=Ressource.objects.filter(responsable=pk).all()
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
        #serializer = UserSerializer(request.user)
        #if serializer.data['role']=='admin':
        queryset=Service.objects.all()
        serializer=ServiceSerializer(queryset ,many=True)
        return Response(serializer.data)
        '''return Response({
            "message":"Vous ne pouvez pas voir tout les services "
        })'''
     def listUserServices(self , request):
        serializers=UserSerializer(request.user)
        if serializers.data['role']=='admin':
            pass
   