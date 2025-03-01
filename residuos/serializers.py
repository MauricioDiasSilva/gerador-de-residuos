# residuos/serializers.py
from rest_framework import serializers
from .models import Residuo

class ResiduoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Residuo
        fields = '__all__'
