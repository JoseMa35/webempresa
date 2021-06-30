from django.db import models
from django.db.models.base import ModelState

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name= "servicio")
    subtitle =models.CharField(max_length=200, verbose_name="Servicios")
    content = models.TextField()
    image = models.ImageField(upload_to="services")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="servicio"
        verbose_name_plural="Servicios"
        ordering = ['-created']

def __str__(self):
    return self.title