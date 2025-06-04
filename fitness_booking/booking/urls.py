from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FitnessViewSet, BookingViewSet, BookingByEmailView

router = DefaultRouter()
router.register(r'classes', FitnessViewSet, basename='fitness')
router.register(r'book', BookingViewSet, basename='booking')

urlpatterns = [
    path('', include(router.urls)),
    path('bookings/', BookingByEmailView.as_view(), name='booking-by-email'),
]
