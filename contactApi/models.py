from django.db import models

# Create your models here.

#from multiselectfield import MultiSelectField

import datetime


class Requestforms(models.Model):
    Reasons = (
        ('1', 'Web Development'),
        ('2', 'App Development'),
        ('3', 'Software Development'),
        ('4', 'General Consultation')
    )
    nameField=models.CharField(default=" ",verbose_name='Your First and Last Name', max_length=200)
    emailField = models.EmailField(default=" ",verbose_name='A valid email address, please.')
    domainCheckField = models.BooleanField(default=True,blank=True)
    urlField = models.URLField(default=" ",verbose_name='Your website', blank=False)
    #servicesRequestingField=MultiSelectField(default=Reasons[0],choices=Reasons)
    descriptionField = models.TextField(default=" ",max_length=20000)
    #dateField = models.DateTimeField(auto_now_add=True, blank=True)




    def __str__(self):
        """A string representation of the model."""
        return self.nameField



