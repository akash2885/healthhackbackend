from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Exercise, ExerciseSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
