from django.shortcuts import render
from djgeojson.views import GeoJSONLayerView

from .models import Municipio


class MunicipioGeoJson(GeoJSONLayerView):
    model = Municipio
    properties = ('popup_content',)


def webmap(request):
    settings_overrides = {
        'DEFAULT_CENTER': (6.0, 45.0),
    }
    context = {
        'settings_overrides': settings_overrides
    }
    return render(request, 'basemap/map.html', context)
