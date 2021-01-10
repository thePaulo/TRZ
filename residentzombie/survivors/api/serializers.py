from rest_framework import serializers
from survivors import models

class SurvivorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Survivors
        fields = '__all__'
        read_only_fields=['infected']

class SurvivorsSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = models.Survivors
        fields = ['infected','latitude','longitude']
        read_only_fields= ['id','name','age','gender','fiji_water','campbell_soup','first_aid_pouch','ak47']
