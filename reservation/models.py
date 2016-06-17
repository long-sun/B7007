from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Instrument(models.Model):
    Instrument_name = models.CharField(max_length=10)
    is_subscribe = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='Instrument_images', blank=True)

    def __str__(self):
        return self.Instrument_name

class Instru(models.Model):
    name = models.ForeignKey(Instrument)
    starttime = models.DateTimeField(blank=True)
    endtime = models.DateTimeField(blank=True)
    phone_num = models.CharField(max_length=11)
    extra_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Anouncement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=10)
    email = models.EmailField()
    pub_date = models.DateTimeField()
    
    def __str__(self):
        return self.title

         
