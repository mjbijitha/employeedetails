from django.urls import path,include
from rest_framework import routers
from .views import Employeeviewset
router=routers.DefaultRouter()
router.register('',Employeeviewset)
urlpatterns = [
    path('details', include(router.urls)),
]