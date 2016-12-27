from django.db import models
from archive.models import Resource
from locations.models import Location
# To support field translations
from hvad.models import TranslatableModel, TranslatedFields


class EventOrganizer(TranslatableModel):
    translations = TranslatedFields(
        organizerName = models.TextField(), # WomenAnticoup, ACA, Youth anticoup, SAC
        organizerType = models.TextField() # Worker, Women, YOuth, ...
    )
    

class Event(models.Model):
    eventType = models.CharField(max_length=100)#CHOICES=['Protest, Human Chain', 'Rally', 'Car Rally', 'Other'])
    # Protest/Human Chain/Rally/Car Rally/..
    eventSize = models.IntegerField(null=True) # Estimate of the number of people in the event
    eventOrganizers = models.ForeignKey(EventOrganizer, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True) # If Available
    location = models.OneToOneField(Location)
    
    createdDate = models.DateTimeField(auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=True)
    

class Link(models.Model):
        link = models.URLField()
        resource = models.ForeignKey(Resource, null=True)

class EventLink(models.Model):
        link = models.ForeignKey(Link)
        event = models.ForeignKey(Event)
