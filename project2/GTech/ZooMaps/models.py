from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.
class Tag(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    tagName = models.CharField(max_length=200, help_text="Enter a tag")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.tagName
                
class User(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    username = models.CharField(max_length=20, help_text="Enter your username")
    password = models.CharField(max_length=20, help_text="Enter your password", default = "")
    emailAddress = models.CharField(max_length=20, help_text="Enter your email address",default = "")
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.username

class Event(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    name = models.CharField(max_length=20, help_text="Enter the name of the Event")
    startDate = models.DateTimeField(blank=True, null=True)  
    endDate = models.DateTimeField(null=True, blank=True)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the Event')
    emoji= models.CharField(max_length=20, help_text="Enter the emojis of the Event");
    latitue = models.FloatField();
    longitude = models.FloatField();
    tags = models.ManyToManyField(Tag, help_text='Select your favorite tags for the Event')
    attendees = models.ManyToManyField(User, help_text='Users going to your Event')
   	
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.name
        
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('event-detail', args=[str(self.id)])
        
class CommentEvent(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    # Fields
    username = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    event = models.ForeignKey('Event', on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=0,validators=[MaxValueValidator(1), MinValueValidator(-1)])
    comment = models.TextField(max_length=1000, help_text='Enter a brief comment for the event')
   	
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.comment
