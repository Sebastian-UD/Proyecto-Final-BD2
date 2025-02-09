from django.db import models

# Create your models here.
class Sede(models.Model):
    cod_sede = models.IntegerField(primary_key=True)
    nombre_sede = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sede'

    def __str__(self):
        return f'cod_sede: {self.cod_sede} nombre_sede: {self.nombre_sede}'