from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name="Titulo",max_length=250)
    slug = models.CharField(verbose_name="Url amigable",max_length=250,unique=True)
    content = models.TextField(verbose_name="Contenido")
    visible = models.BooleanField(verbose_name="Visible")
    order = models.IntegerField(default=0,verbose_name="Orden")

    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Creado")
    class Meta:
        verbose_name ="Página"
        verbose_name_plural = "Páginas"

    def __str__(self):
        return self.title