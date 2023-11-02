from .models import Sleep
from rest_framework import serializers


class SleepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sleep
        fields = '__all__'