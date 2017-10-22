from django import forms
from leaflet.forms.widgets import LeafletWidget

from .models import Terreno


class TerrenoForm(forms.ModelForm):
    class Meta:
        model = Terreno
        fields = ('endereco', 'geom')
        widgets = {'geom': LeafletWidget()}
