from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.
    
class RateEventForm(forms.Form):
    rating = forms.IntegerField(help_text="Enter a rating between -1 and 1.")

    def clean_renewal_date(self):
        data = self.cleaned_data['rating']
        
        #Check rating is -1, 0 or 1. 
        if not ((rating ==1) or (rating ==0) or (rating == -1)):
            raise ValidationError(_('Invalid rating - renewal in past'))

        # Remember to always return the cleaned data.
        return data
        
class CommentEventForm(forms.Form):
    message = forms.CharField(help_text="Enter your message.")

    def clean_renewal_date(self):
        data = self.cleaned_data['message']
        
        #Check that message is not empty. 
        if not (message):
            raise ValidationError(_('Nothing has been entered'))

        # Remember to always return the cleaned data.
        return data
        
class AttendEventForm(forms.Form):
    answer = forms.BooleanField(help_text="Want to attend?")

    def clean_renewal_date(self):
        data = self.cleaned_data['coming?']
        
        #Check that message is not empty. 
        if not (answer):
            raise ValidationError(_('You do not want to go?'))

        # Remember to always return the cleaned data.
        return data
        
class UnAttendEventForm(forms.Form):
    answer = forms.BooleanField(help_text="Don't want to go anymore?")

    def clean_renewal_date(self):
        data = self.cleaned_data['not coming?']
        
        #Check that message is not empty. 
        if not (answer):
            raise ValidationError(_('You do want to go?'))

        # Remember to always return the cleaned data.
        return data