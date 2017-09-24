from django.conf.urls import url

from .views import MunicipioGeoJson, MapView

urlpatterns = [
    url(r'^$', MapView.as_view(), name='mapa'),
    url(r'^municipios.geojson$', MunicipioGeoJson.as_view(), name='municipios_geojson'),
]
