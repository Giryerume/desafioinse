from rest_framework import serializers
from .models import Inse

class InseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inse
        fields = '__all__'
