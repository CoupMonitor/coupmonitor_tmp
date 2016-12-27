from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from .widgets import LocationPickerWidget

class LocationPickerField(forms.MultiValueField):
    default_error_messages = {
        'invalid': ('Enter a valid geoposition.')
    }

    def __init__(self, *args, **kwargs):
        self.widget = LocationPickerWidget
        fields = (
            forms.FloatField(label = _('latitude')),
            forms.FloatField(label = _('longitude'))
        )

        if 'initial' in kwargs:
            kwargs['initial'] = LocationPicker(*kwargs['initial'].split(','))


        super(LocationPickerField, self).__init__(fields, **kwargs)


    def widget_attrs(self, widget):
        classes = widget.attrs.get('class', '').split()
        classes.append('locationpicker')
        return {'class': ' '.join(classes)}

    def compress(self, value_list):
        if value_list:
            return value_list
        return ""




