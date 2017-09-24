# gerado através do comando:
# m ogrinspect data/municipios_pb.shp Municipio --mapping --srid 4326 --multi

from django.contrib.gis.db import models


class Municipio(models.Model):
    geocode = models.CharField(max_length=12)
    nome = models.CharField(max_length=50)
    meso = models.CharField(max_length=50)
    micro = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.nome

    @property
    def popup_content(self):
        popup = "<strong>Nome:</strong> {} <br>".format(self.nome)
        popup += "<strong>Geocódigo:</strong> {} <br>".format(self.geocode)
        popup += "<strong>Mesoregião:</strong> {} <br>".format(self.meso)
        popup += "<strong>Microregião:</strong> {} <br>".format(self.micro)
        return popup

    class Meta:
        db_table = 'municipios'
        ordering = ['nome', ]
        verbose_name = 'municipio'
        verbose_name_plural = 'municipios'
