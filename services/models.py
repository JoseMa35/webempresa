from django.db import models
from django.db.models.base import ModelState

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name= "Titulo")
    subtitle =models.CharField(max_length=200, verbose_name="Servicio")
    content = models.TextField()
    image = models.ImageField(upload_to="services")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Titulo"
        verbose_name="Servicio"

def __str__(self):
    return self.title