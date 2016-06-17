from django import forms
from rango.models import Instrument, Instru
from django.contrib.auth.models import User

class InstrumentForm(forms.Form):
    class Meta:
        model = Instrument
        fields = ('Instrument_name', 'is_subcribe', 'picture')

