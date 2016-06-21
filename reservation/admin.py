from django.contrib import admin
from reservation.models import Instrument
# Register your models here.

class InstrumentAdmin(admin.ModelAdmin):
    #fields = ['category', 'title', 'url', 'views']
    fieldsets = [
        (None, {'fields': ['Instrument_name']}),
        ('Detail information', {'fields': ['is_subscribe', 'picture']})
        ]
    list_display = ('Instrument_name', 'is_subscribe')


admin.site.register(Instrument, InstrumentAdmin)
