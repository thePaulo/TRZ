from rest_framework import viewsets
from items.api import serializers
from items import models
from rest_framework.exceptions import PermissionDenied
from rest_framework import mixins

class ItemsViewSet( mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.ItemsSerializer
    queryset = models.Item.objects.all()

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.request.method == 'PUT':
            #serializer_class = serializers.ItemsSerializerUpdate
            raise PermissionDenied('Você não tem permissão de modificar Items')

        if self.request.method == 'POST':
            raise PermissionDenied('Você não tem permissão de criar Items')

        if self.request.method == 'delete':
            raise PermissionDenied('Você não tem permissão de deletar Items')

        return serializer_class
