from rest_framework import serializers
from .models import Services

class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'