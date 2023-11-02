from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Diet, DietSerializer


class DietViewSet(viewsets.ModelViewSet):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer
