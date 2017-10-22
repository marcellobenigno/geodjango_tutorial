from django.contrib.gis.db import models


class Terreno(models.Model):
    endereco = models.CharField('endereço', max_length=100)
    geom = models.PolygonField(srid=4326)

    def __str__(self):
        return self.endereco
