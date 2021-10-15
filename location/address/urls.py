
from django.urls import path
from .views import getGeology

urlpatterns = [
    path('', getGeology)
]