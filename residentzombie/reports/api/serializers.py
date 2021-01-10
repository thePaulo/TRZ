from rest_framework import serializers
from reports import models

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = '__all__'
