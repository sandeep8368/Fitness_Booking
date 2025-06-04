from rest_framework import serializers
from .models import BookingModel, FitnessModel


class FitnessSerializer(serializers.Serializer):
    class Meta:
        model = FitnessModel
        fields = '__all__'
        
        
class BookingSerializer(serializers.Serializer):
    class Meta:
        model = BookingModel
        fields = '__all__'
        
        
    def validate(self, data):
        fitness_class = data['fitness_class']
        if fitness_class.available_slots <= 0:
            raise serializers.ValidationError("No slots available")
        return data