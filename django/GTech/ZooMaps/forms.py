from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime
    
class RateEventForm(forms.Form):
    rating = forms.IntegerField(help_text="Enter a rating between -1 and 1.")

    def clean_rating(self):
        data = self.cleaned_data['rating']
        
        #Check rating is -1, 0 or 1. 
        if not ((data ==1) or (data ==0) or (data == -1)):
            raise ValidationError(_('Invalid rating - rate only using -1, 0, or 1'))

        # Remember to always return the cleaned data.
        return data
        
class CommentEventForm(forms.Form):
    message = forms.CharField(help_text="Enter your message.")

    def clean_message(self):
        data = self.cleaned_data['message']
        
        #Check that message is not empty. 
        if not (data):
            raise ValidationError(_('Nothing has been entered'))

        # Remember to always return the cleaned data.
        return data
        
class AttendEventForm(forms.Form):
    answer = forms.BooleanField(help_text="You would like to attend?")
    
    def clean_answer(self):
        data = self.cleaned_data['answer']
        
        #Check that event is in the future. 
        #if data.date < datetime.date.today():
         #   raise ValidationError(_('Cannot go, it is in the past!'))

        # Remember to always return the cleaned data.
        return data
        
class UnAttendEventForm(forms.Form):
    answer = forms.BooleanField(help_text="Don't want to go anymore?")

    def clean_answer(self):
        data = self.cleaned_data['answer']
        
        #Check. 
        #if not (answer):
         #   raise ValidationError(_('You do want to go?'))

        # Remember to always return the cleaned data.
        return data


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LogOnForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    address_email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'address_email', 'password1', 'password2', )