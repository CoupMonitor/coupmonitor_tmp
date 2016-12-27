# -*- coding: utf-8 -*-

from hvad import forms as hvforms
from django import forms
from .models import Location
from django.utils.translation import ugettext_lazy as _

from jquery_locationpicker.fields import LocationPickerField
from jquery_locationpicker.widgets import LocationPickerWidget

class LocationForm(hvforms.TranslatableModelForm):
    name = forms.CharField()
    governorate = forms.CharField()
    location = LocationPickerField(widget=LocationPickerWidget)


class LocationFormArabic(LocationForm):

    class Meta:
        model = Location
        fields = ['name', 'governorate', 'location']

        labels = {
            'name': _('إسم المنطقة'),
            'governorate': _('المحاقظة'),
        }

    def save():
        pass

class LocationFormEnglish(LocationForm):
    class Meta:
        model= Location
        fields = ['name', 'governorate']

        labels = {
            'name': _('Name'),
            'governorate': _('Governorate'),
        }


