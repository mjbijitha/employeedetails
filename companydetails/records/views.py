from django.shortcuts import render

from rest_framework import viewsets
from .models import employee1
from .serializer import EmployeeSerializer
class Employeeviewset(viewsets.ModelViewSet):
    queryset = employee1.objects.all()
    serializer_class = EmployeeSerializer

# Create your views here.
