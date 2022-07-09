from django.db import models

# Create your models here.


class Persona(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    birth_date = models.DateField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
