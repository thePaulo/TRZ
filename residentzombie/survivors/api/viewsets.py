from rest_framework import viewsets
from survivors.api import serializers
from survivors import models

class SurvivorsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SurvivorsSerializer
    queryset = models.Survivors.objects.all()
