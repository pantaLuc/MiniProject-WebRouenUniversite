from django.contrib import admin
from .models import Ressource , Localisation , Anomalie ,Service , AnomalieRessource
# Register your models here.
admin.site.register(Ressource)
admin.site.register(Localisation)
admin.site.register(Anomalie)
admin.site.register((Service))
admin.site.register(AnomalieRessource)