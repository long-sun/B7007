from django.db import models
from userprofile.models import UserProfile

# Create your models here.


class Instrument(models.Model):
    title = models.CharField(max_length=10)
    is_subscribe = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='Instrument_images', blank=True)

    def __str__(self):
        return self.title


class Subscribe(models.Model):
    instrument = models.ForeignKey(Instrument)
    user = models.ForeignKey(UserProfile)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
