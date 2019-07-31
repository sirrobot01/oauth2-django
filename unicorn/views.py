from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

from . import models, serializer

class UnicornViewSet(viewsets.ModelViewSet):
    queryset = models.Unicorn.objects.all()
    serializer_class = serializer.UnicornSerializer

