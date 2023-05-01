from django.db import models
from django.utils import timezone
from dateutil.relativedelta import relativedelta

class Liquor(models.Model):
    destilado = models.CharField(max_length=50,default='alcohol',blank=True) 
    nombre = models.CharField (max_length=50,default='???',blank=True) 
    description = models.TextField(default='Licor',blank=True)
    paisOrigen= models.CharField (max_length=50,default='Mexico',blank=True)
    size = models.CharField (max_length=50,default='1L',blank=True)
    tipoEnvase = models.CharField (max_length=50,default='Botella de cristal',blank=True)
    fechaIngreso = models.DateField (default=timezone.now)
    caducidad = models.DateField (default= timezone.datetime.today() + relativedelta(months=+3))
    edicion = models.CharField (max_length=50,default='Standar')
    precio = models.FloatField (default=1000)