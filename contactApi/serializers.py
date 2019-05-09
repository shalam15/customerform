from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Requestforms 



class WebsiteContactForm(serializers.ModelSerializer):
    class Meta:
        model = Requestforms
        fields =('nameField', 'emailField', 'domainCheckField','urlField','descriptionField' )