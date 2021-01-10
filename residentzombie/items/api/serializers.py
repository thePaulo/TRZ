from rest_framework import serializers
from items import models

class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'
        read_only_fields=['points','name','owner']

class ItemsSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'
