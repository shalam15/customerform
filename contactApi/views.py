from django.shortcuts import render
from rest_framework import generics
from contactApi.models import Requestforms
from contactApi.serializers import  WebsiteContactForm


# Create your views here.
class UserViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows users to submit forms.
    """
    queryset = Requestforms.objects.all()
    serializer_class = WebsiteContactForm

class DetailCustomerRequest(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that shows users one by one.
    """
    queryset = Requestforms.objects.all()
    serializer_class = WebsiteContactForm