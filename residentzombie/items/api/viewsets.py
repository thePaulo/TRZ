from rest_framework import viewsets, mixins
from items.api import serializers
from items import models

'''class ItemsViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):'''
class ItemsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ItemsSerializer
    queryset = models.Item.objects.all()
