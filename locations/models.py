from django.db import models
from hvad.models import TranslatableModel, TranslatedFields
# An important question is wether we need to use
# GeoDjango featuers in this app

class Location(TranslatableModel):

    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    
    # These fields exist in multiple languages  
    translations = TranslatedFields(
        name = models.CharField(max_length=300),
        governorate = models.CharField(max_length=300)
    )

    unique_together = (("name", "governorate"),)
    def __unicode__(self):
        return "%s, %s" % (self.name, self.governorate)

