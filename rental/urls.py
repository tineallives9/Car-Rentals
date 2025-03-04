from django.urls import path
from .views import BookingListCreateAPIView, BookingRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('rental/', BookingListCreateAPIView.as_view(), name='rental-list-create'),
    path('rental/<int:pk>/', BookingRetrieveUpdateDestroyAPIView.as_view(), name='rental-retrieve-update-destroy')
]