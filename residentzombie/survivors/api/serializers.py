from rest_framework import serializers
from survivors import models

class SurvivorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Survivors
        fields = '__all__'
