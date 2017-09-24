from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Municipio

admin.site.register(Municipio, LeafletGeoAdmin)
