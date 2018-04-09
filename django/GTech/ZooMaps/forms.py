from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime
    
class RateEventForm(forms.Form):
    rating = forms.IntegerField(help_text="Enter a rating between -1 and 1.")

    def clean_renewal_date(self):
        data = self.cleaned_data['rating']
        
        #Check rating is -1, 0 or 1. 
        if not ((data ==1) or (data ==0) or (data == -1)):
            raise ValidationError(_('Invalid rating - rate only using -1, 0, or 1'))

        # Remember to always return the cleaned data.
        return data
        
class CommentEventForm(forms.Form):
    message = forms.CharField(help_text="Enter your message.")

    def clean_renewal_date(self):
        data = self.cleaned_data['message']
        
        #Check that message is not empty. 
        if not (data):
            raise ValidationError(_('Nothing has been entered'))

        # Remember to always return the cleaned data.
        return data
        
class AttendEventForm(forms.Form):
    answer = forms.BooleanField(help_text="Want to attend?")

    def clean_renewal_date(self):
        data = self.cleaned_data['answer']
        
        #Check that message is not empty. 
        if event.date < datetime.date.today():
            raise ValidationError(_('Cannot go, it is in the past!'))

        # Remember to always return the cleaned data.
        return data
        
class UnAttendEventForm(forms.Form):
    answer = forms.BooleanField(help_text="Don't want to go anymore?")

    def clean_renewal_date(self):
        data = self.cleaned_data['answer']
        
        #Check that message is not empty. 
        if not (answer):
            raise ValidationError(_('You do want to go?'))

        # Remember to always return the cleaned data.
        return data