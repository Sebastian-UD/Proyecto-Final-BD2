from django.db import models
from sede.models import Sede

# Create your models here.
class Pregrado(models.Model):
    cod_pregrado = models.IntegerField(primary_key=True)
    cod_sede = models.ForeignKey(Sede, on_delete=models.CASCADE, db_column='cod_sede')
    region = models.CharField(max_length=100)
    nombre = models.CharField(max_length=120)
    creditos = models.IntegerField()
    nota_minima = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pregrado'

    def __str__(self):
        return f'Codigo: {self.cod_pregrado} sede: {self.cod_sede.cod_sede} region: {self.region} nombre: {self.nombre} creditos: {self.creditos} nota_min: {self.nota_minima}'