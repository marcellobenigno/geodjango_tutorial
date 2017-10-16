from django.contrib.gis.geos import GEOSGeometry
from django.test import TestCase

from ..models import Municipio


class MunicipioTest(TestCase):
    def setUp(self):
        geom = GEOSGeometry(
            "MultiPolygon(((-38.278 -6.278, -38.275 -6.381, -38.1880 -6.378, -38.1932 -6.280, -38.278 -6.278)))")

        self.obj = Municipio.objects.create(
            geocode='123456',
            nome='Água Branca',
            meso='Sertão Paraibano',
            micro='Serra do Teixeira',
            geom=geom)

    def test_create(self):
        self.assertTrue(Municipio.objects.exists())

    def test_str(self):
        self.assertEqual('Água Branca', str(self.obj))

    def test_ordering(self):
        self.assertListEqual(['nome'], Municipio._meta.ordering)
