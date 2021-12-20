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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ressources/' , include('ressources.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/users/', include('users.urls')), # new
     path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('openapi', get_schema_view( # new
    title="Gestionnaire de Maintenance ",
    description="Une Liste des API utiliser pour construire la solution ",
    version="1.0.0"
    ), name='openapi-schema'),
]
