from django.shortcuts import get_object_or_404
from .models import FitnessModel, BookingModel
from .serializers import FitnessSerializer, BookingSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
# Create your views here.



class FitnessViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = FitnessModel.objects.all()
        serializer = FitnessSerializer(queryset, many = True)
        return Response(serializer.data)
    

class BookingViewSet(viewsets.ViewSet):
    def create(self,request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            fitness_class = serializer.validated_data['fitness_class']
            if fitness_class.available_slots <= 0:
                return Response({"error" : "No slots available."}, status  = status.HTTP_400_BAD_REQUEST)
            
            booking = serializer.save()
            fitness_class.available_slots -=1
            fitness_class.save()
            
            return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class BookingByEmailView(APIView):
    def get(self, request):
        email = request.query_params.get('email')
        if not email:
            return Response({"errors" : "EMAIL query param is required."}, status=400)
        
        bookings = BookingModel.objects.filter(client_email=email)
        serializer = BookingSerializer(bookings, many = True)
        return Response(serializer.data)
    