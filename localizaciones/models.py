from django.db import models

# Create your models here.
class locations(models.Model):
    nombre = models.CharField(verbose_name="Nombre Español",max_length=20)
    code = models.CharField(verbose_name="Nombre código",max_length=20)
    pais = models.CharField(verbose_name="Pais",max_length=20)

    class Meta:
        verbose_name ="Location"
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.nombre