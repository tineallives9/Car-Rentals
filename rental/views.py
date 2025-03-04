from django.shortcuts import render

from rest_framework import generics

from .serializers import BookingSerializer
from .models import Booking

# Create your views here.

class BookingListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    
    
class BookingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()