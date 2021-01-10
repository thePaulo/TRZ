from rest_framework import viewsets, mixins
from reports.api import serializers
from reports import models

class ReportViewSet(mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = serializers.ReportSerializer
    queryset = models.Report.objects.all()
