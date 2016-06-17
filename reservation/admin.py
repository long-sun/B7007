from django.contrib import admin
from reservation.models import Instrument, Instru
# Register your models here.

class InstrumentAdmin(admin.ModelAdmin):
    #fields = ['category', 'title', 'url', 'views']
    fieldsets = [
        (None, {'fields': ['Instrument_name']}),
        ('Detail information', {'fields': ['is_subscribe', 'picture']})
        ]
    list_display = ('Instrument_name', 'is_subscribe')

class InstruAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Date information', {'fields': ['starttime', 'endtime']}),
        ('Extra information', {'fields': ['phone_num', 'extra_info']})
        ]
    list_display = ('name', 'starttime', 'endtime', 'extra_info')    



admin.site.register(Instrument, InstrumentAdmin)
admin.site.register(Instru, InstruAdmin)
