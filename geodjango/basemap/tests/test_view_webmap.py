from django.contrib.gis.geos import GEOSGeometry
from django.shortcuts import resolve_url as r
from django.test import TestCase

from ..models import Municipio


class WebMap(TestCase):
    def setUp(self):
        geom = GEOSGeometry(
            "MultiPolygon(((-38.278 -6.278, -38.275 -6.381, -38.1880 -6.378, -38.1932 -6.280, -38.278 -6.278)))")

        self.obj = Municipio.objects.create(
            geocode='123456',
            nome='Água Branca',
            meso='Sertão Paraibano',
            micro='Serra do Teixeira',
            geom=geom)

        self.response = self.client.get(r('basemap:webmap'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'basemap/map.html')
