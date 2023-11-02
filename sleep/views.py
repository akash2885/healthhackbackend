from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Sleep, SleepSerializer


class SleepViewset(viewsets.ModelViewSet):
    queryset = Sleep.objects.all()
    serializer_class = SleepSerializer
