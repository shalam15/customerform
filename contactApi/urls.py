from django.urls import path
from contactApi import views

urlpatterns = [
    path('', views.UserViewSet.as_view())
]
