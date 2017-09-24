from django.views.generic import TemplateView
from djgeojson.views import GeoJSONLayerView

from .models import Municipio


class MunicipioGeoJson(GeoJSONLayerView):
    model = Municipio
    properties = ('popup_content',)


class MapView(TemplateView):
    template_name = 'basemap/map.html'
