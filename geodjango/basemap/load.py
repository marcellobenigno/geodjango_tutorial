# -*- coding: utf-8 -*-
# após rodar as migrações, digite no terminal:
# m shell_plus
# >>> from geodjango.basemap.load import run
# >>> run()
#

import os

from django.contrib.gis.utils import LayerMapping

from .models import Municipio

municipio_mapping = {
    'geocode': 'geocode',
    'nome': 'nome',
    'meso': 'meso',
    'micro': 'micro',
    'geom': 'MULTIPOLYGON',
}

municipios_shp = os.path.abspath(os.path.join('municipios_pb.shp'))


def run(verbose=True):
    lm1 = LayerMapping(Municipio, municipios_shp, municipio_mapping)
    lm1.save(strict=True, verbose=verbose)
