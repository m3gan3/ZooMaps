from django.db import models

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
    name = models.CharField(max_length=20, help_text="Enter the name of the Location")
   	
   	
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
    name = models.CharField(max_length=20, help_text="Enter the name of the event")
   	
   	
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.name