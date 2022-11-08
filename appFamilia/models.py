from unittest.util import _MAX_LENGTH
from django.db import models
import datetime

# Create your models here.

class Familiar(models.Model):

    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    relacion = models.CharField(max_length=50)
    ocupacion = models.CharField(max_length=50)
    fechanac = models.DateField(default=datetime.datetime.today())



