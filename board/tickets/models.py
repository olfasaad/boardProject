from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=50)
    hall=models.CharField(max_length=10)
    date=models.DateField(max_length=10)

class Guest (models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)

class Reservation(models.Model):
    movie=models.ForeignKey(Movie,related_name="reservations",on_delete=models.CASCADE)
    guest=models.ForeignKey(Guest,related_name="reservations",on_delete=models.CASCADE)