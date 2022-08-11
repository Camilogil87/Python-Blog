from datetime import datetime
from operator import length_hint
from unicodedata import name
from django.db import models

# Create your models here.
class familiares(models.Model):
    nombre=models.CharField(max_length=40)
    dni=models.IntegerField()
    Fecha_nacimiento=models.DateField(max_length=40)