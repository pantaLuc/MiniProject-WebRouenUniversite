from django.urls import path

from ressources.views import  AdminGestion, CreerAnomalie, CreerLocalisation, CreerRessource, CreerService, GestResponsable, ListLocalisation, RUDAnomalie, RUDLocalisation, RUDRessource, RUDService, SignalerAnomalie

urlpatterns = [
  path ('ressource/<int:pk>',RUDRessource.as_view()),
  path('ressource', CreerRessource.as_view()),
  path('anomalie' , CreerAnomalie.as_view()),
  path('anomalie/<int:pk>',RUDAnomalie.as_view()) ,
  path('service/<int:pk>',RUDService.as_view()),
  path('service' , CreerService.as_view()),
  path('localisation' , CreerLocalisation.as_view()),
  path('localisation/<int:pk>' , RUDLocalisation.as_view()),
  path('lisLocalisation/' , ListLocalisation.as_view()),
  path('signalerAnomalie' ,SignalerAnomalie.as_view()),
  path('responsable/ressources/<int:pk>' , GestResponsable.as_view({
      'get':'ressourceResponsable',
  })),
  path('responsable/anomalie/<int:pk>' , GestResponsable.as_view({
      'get':'anomalieRessource',
  })),
path('listServices/' ,AdminGestion.as_view({
    'get':'listServices',
})),
]