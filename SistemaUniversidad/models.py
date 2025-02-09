from django.db import models

# Create your models here.
class Sede(models.Model):
    cod_sede = models.IntegerField(primary_key=True)
    nombre_sede = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sede'
    
    def __str__(self):
        return f'cod_sede: {self.cod_sede} | nombre_sede: {self.nombre_sede}'
    
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
        return f'Codigo: {self.cod_pregrado} | sede: {self.cod_sede.cod_sede} | region: {self.region} | nombre: {self.nombre} | creditos: {self.creditos} | nota_min: {self.nota_minima}'

class Asignatura(models.Model):
    cod_asignatura = models.IntegerField(primary_key=True)
    cod_pregrado = models.ForeignKey(Pregrado, on_delete=models.CASCADE, db_column='cod_pregrado')
    nombre_asignatura = models.CharField(max_length=60)
    horas_semanales = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'asignatura'

    def __str__(self):
        return f'cod_asignatura: {self.cod_asignatura} | cod_pregrado: {self.cod_pregrado.cod_pregrado} | nombre_asignatura: {self.nombre_asignatura} | horas_semanales: {self.horas_semanales}'

class Curso(models.Model):
    cod_pregrado_curso = models.IntegerField(primary_key=True)
    cod_asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, db_column='cod_asignatura')
    capacidad_estudiantes = models.IntegerField()
    nombre_curso = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'curso'

    def __str__(self):
        return f'cod_pregrado_curso: {self.cod_pregrado_curso} | cod_asignatura: {self.cod_asignatura.cod_asignatura} | capacidad_estudiantes: {self.capacidad_estudiantes} | nombre_curso: {self.nombre_curso}'

class Grupo(models.Model):
    cod_grupo = models.IntegerField(primary_key=True)
    cod_pregrado_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, db_column='cod_pregrado_curso')
    semestre = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'grupo'
    
    def __str__(self):
        return f'cod_grupo: {self.cod_grupo} | cod_pregrado_curso: {self.cod_pregrado_curso.cod_pregrado_curso} | semestre: {self.semestre}'

class Clasificacion(models.Model):
    categoria = models.CharField(primary_key=True, max_length=30)
    num_max_horas = models.IntegerField()
    sueldo = models.FloatField()

    class Meta:
        managed = False
        db_table = 'clasificacion'

    def __str__(self):
        return f'categoria: {self.categoria} | num_max_horas: {self.num_max_horas} | sueldo: {self.sueldo}'

class Profesor(models.Model):
    numero_documento = models.IntegerField(primary_key=True)
    categoria = models.ForeignKey(Clasificacion, on_delete=models.CASCADE, db_column='categoria')
    nombre_profesor = models.CharField(max_length=120)
    direccion = models.CharField(max_length=60)
    telefono = models.CharField(max_length=15)
    e_mail = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'profesor'

    def __str__(self):
        return f'numero_documento: {self.numero_documento} | categoria: {self.categoria.categoria} | nombre_profesor: {self.nombre_profesor} | direccion: {self.direccion} | telefono: {self.telefono} | e_mail: {self.e_mail}'
    
class Dicta(models.Model):
    cod_grupo = models.OneToOneField('Grupo', on_delete=models.CASCADE, db_column='cod_grupo', primary_key=True)  # The composite primary key (cod_grupo, numero_documento) found, that is not supported. The first column is selected.
    numero_documento = models.ForeignKey('Profesor', on_delete=models.CASCADE, db_column='numero_documento')
    n_horas = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dicta'
        unique_together = (('cod_grupo', 'numero_documento'), ('cod_grupo', 'numero_documento'),)

    def __str__(self):
        return f'cod_grupo: {self.cod_grupo.cod_grupo} | numero_documento: {self.numero_documento.numero_documento} | n_horas: {self.n_horas}'

class Nomina(models.Model):
    id_nomina = models.IntegerField(primary_key=True)
    numero_documento = models.ForeignKey(Profesor, on_delete=models.CASCADE, db_column='numero_documento', blank=True, null=True)
    salario = models.DecimalField(max_digits=8, decimal_places=5)
    mes = models.IntegerField()
    anio = models.IntegerField()
    horas_trabajadas = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nomina'

    def __str__(self):
        return f'id_nomina: {self.id_nomina} | numero_documento: {self.numero_documento.numero_documento} | salario: {self.salario} | mes: {self.mes} | anio: {self.anio} | horas_trabajadas: {self.horas_trabajadas}'