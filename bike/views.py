from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Bike
from .serializers import BikeSerializer


# Create your views here.
class BikeListView(ListCreateAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer


class BikeDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer