from django.urls import path

from ressources.views import  AdminGestion, CreerAnomalie, CreerLocalisation, CreerRessource, CreerService, GestResponsable, ListAnomalieSignalerParRessource, ListAnomalies, ListLocalisation, ListRessource, RUDAnomalie, RUDLocalisation, RUDRessource, RUDService, RessourceLocalisation, SignalerAnomalie, SignalerAnomalieExistante

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
  path('listesAnomalies/' , ListAnomalies.as_view({
      'get':'get',
  })),
   path('anomalieExistant/<int:pk>',SignalerAnomalieExistante.as_view({
       'put':'update',
   }),name='updateAnomalieExistante'),
   
  path('signalerAnomalie/', SignalerAnomalie.as_view()),
  path('listeAnomalieParRessource/<int:pk>',ListAnomalieSignalerParRessource.as_view({
      'get':'get',
  })),
  path('responsable/ressources/<int:pk>' , GestResponsable.as_view({
      'get':'ressourceResponsable',
  })),
  path('responsable/anomalie/<int:pk>' , GestResponsable.as_view({
      'get':'anomalieRessource',
  })),
path('listServices/' ,AdminGestion.as_view({
    'get':'listServices',
})),
path('listRessource/' , ListRessource.as_view({
    'get':'get'
})),

path('ressourcesLocalisation/<int:pk>' ,RessourceLocalisation.as_view({
    'get':'get'
})),
]