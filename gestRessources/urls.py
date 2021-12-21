"""gestRessources URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from rest_framework.schemas import get_schema_view # new
from rest_framework import permissions # new
from drf_yasg.views import get_schema_view # new
from drf_yasg import openapi # new

schema_view = get_schema_view( # new
openapi.Info(
title="We Report It ",
default_version="v1",
description=""" L’une des plus grandes problématiques dans le cadre de la maintenance des infrastructures d’une organisation
consiste en la détection des défaillances ou de l’épuisement des fournitures de ces infrastructures. Cela requiert du
personnel avec des tâches dédiées au contrôle périodique de ces infrastructures, en particulier pour celles qui ne sont
pas connectées.
Une alternative peut consister à permettre aux usagers de ces infrastructures de signaler des anomalies lorsqu’elle
apparaissent à condition que ces tâches de signalement s’eﬀectuent de la façon la plus simples et la plus eﬃcace
possible. Toute étape superﬂue (par rapport au processus de signalement) aura tendance à dissuader l’usager de sa
contribution.
Le processus de signalement consiste à réaliser les étapes suivantes :
1. identiﬁer la ressource (élément d’infrastructure) défaillante ; ex : vidéo-projecteur en libre service, éclairage
d’une salle, distributeur de fournitures sanitaires (savon, essuie-main, etc), ... ;
2. localiser la ressource défaillante ; ex : salle courrier, salle U2.2.2, ... ;
3. formuler le problème rencontré par la ressource ; ex : ampoule grillée, câble/prise défaillante, réservoir vide, ... ;
4. identiﬁer la personne ou le service responsable de la maintenance de la ressource,
5. eﬀectuer la transmission de ces informations au responsable de la maintenance de la ressource.\n
Nous avons construit une platforme Pour simplifier le Processus .Cette Page donne la Description des Endpoints a utiliser """,
terms_of_service="https://www.google.com/policies/terms/",
contact=openapi.Contact(email="luc-perin.panta-pameni@univ-rouen.fr"),
license=openapi.License(name="Université de Rouen"),
),
public=True,
permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ressources/' , include('ressources.urls')),
    #path('api-auth/', include('rest_framework.urls')),
    path('api/users/', include('users.urls')), # new
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('swagger/', schema_view.with_ui( # new
'swagger', cache_timeout=0), name='schema-swagger-ui'),
path('redoc/', schema_view.with_ui( # new
'redoc', cache_timeout=0), name='schema-redoc'),

]
