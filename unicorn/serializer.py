from rest_framework import serializers
from . import models

class UnicornSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Unicorn
        fields = '__all__'
