from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.

class User(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    username = models.CharField(max_length=20, help_text="Enter your username")
   	
   	
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.username
        
class Place(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    name = models.CharField(max_length=20, help_text="Enter the name of the Place")
    address = models.CharField(max_length=40, help_text="Enter the address of the Place")
   	
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.name
    
class Event(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    name = models.CharField(max_length=20, help_text="Enter the name of the Event")
    location = models.ForeignKey('Place', on_delete=models.SET_NULL, null=True)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the Event')
    PRIVATE_CHOICES= (
        ('pr','Private'),
        ('pu','Public'),
    )
    private = models.CharField(max_length=2, choices=PRIVATE_CHOICES, default = 'pr')
   	
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.name