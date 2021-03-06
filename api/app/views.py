from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets

from .serializers import LocationSerializer
from .models import Location

# Create your views here.

# def index (request):
#     return HttpResponse("Cool Glidings")

class LocationViewSet (viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
