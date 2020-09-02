from django import forms
import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
# ^ Django's translation fucntions

class SelectTrip(forms.Form):
    start_date = forms.DateField(required = True, help_text = "Enter the date you would like to start your trip.")

    end_date = forms.DateField(required = True, help_text = "Enter the date you would like to end your trip.")

    trip_type = forms.CharField(required = True, help_text = "Please enter the type of trip you would like to take.")

    def clean_end_date(self):
        # use clean() to clean multiple inputs and return self.cleaned_data
        data = self.cleaned_data['end_date']
        #start_data = self.cleaned_data['start_date']
        #type_data = self.cleaned_data['trip_type']
        # get above data and return whether or not we use it

        if data < self.start_date:
            raise ValidationError(_('Invalid end date!'))

        return data