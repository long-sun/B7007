from django import forms
from rango.models import Instrument, Subscribe


class InstrumentForm(forms.ModelForm):

    class Meta:
        model = Instrument
        fields = ('Instrument_name', 'is_subcribe', 'picture')


class SubscribeForm(forms.ModelForm)

    class Meta:
        model = Subscribe
        fields = ('Instrument', 'start_time', 'end_time')
