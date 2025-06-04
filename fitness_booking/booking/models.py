from django.db import models

# Create your models here.
class FitnessModel(models.Model):
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    instructor = models.CharField(max_length=100)
    available_slots = models.PositiveIntegerField()
    
    
    
class BookingModel(models.Model):
    fitness_class = models.ForeignKey(FitnessModel, on_delete = models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()