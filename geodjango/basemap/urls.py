from django.conf.urls import url

from .views import MunicipioGeoJson, webmap

urlpatterns = [
    url(r'^$', webmap, name='webmap'),
    url(r'^municipios.geojson$', MunicipioGeoJson.as_view(), name='municipios_geojson'),
]
