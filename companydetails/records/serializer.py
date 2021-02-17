from rest_framework import serializers
from .models import employee1
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=employee1
        fields='__all__'