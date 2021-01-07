from rest_framework import viewsets
from survivors.api import serializers
from survivors import models

class SurvivorsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.SurvivorsSerializer
    queryset = models.Survivors.objects.all()

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            serializer_class = serializers.SurvivorsSerializerUpdate

        return serializer_class
