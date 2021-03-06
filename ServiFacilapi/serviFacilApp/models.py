from djongo import models
from django import forms
# Create your models here.

class Direccion(models.Model):
    calle_principal = models.CharField(max_length=120, default='NA')
    calle_secundaria = models.CharField(max_length=120, default='NA')
    numero_local = models.CharField(max_length=120, default='S/N')


class Persona(models.Model):
    cedula = models.CharField(max_length=20)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(default="2010-02-02")
    telefono = models.CharField(max_length=10, null=True, blank=True)
    direccion = models.CharField(max_length=150, null=True, blank=True)
    #direccion = models.EmbeddedField(
     #   model_container=Direccion, null=False, blank=False
    #)

    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)
class TipoUser(models.Model):
    nombre = models.CharField(max_length=10, unique=True)
    descripcion = models.CharField(max_length=150)
    def __str__(self):
        return '{}'.format(self.nombre)


class Usuarios(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=20)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE,
                                   null=False, blank=False)
    tipo_ususario = models.ForeignKey(TipoUser, on_delete=models.CASCADE,
                                   null=False, blank=False)
    def __str__(self):
        return '{}'.format(self.username)

class Empresa(models.Model):
    ruc = models.CharField(max_length=13, unique=True)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150, null=True, blank=True)
    #direccion = models.EmbeddedField(
     #   model_container=Direccion
    #)
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)

class Servicio(models.Model):
    nombre = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.CharField(max_length=150)
    empresa = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.nombre)

class Turno(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.CharField(max_length=150)
    persona = models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, null=True, blank=True, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, null=True, blank=True, on_delete=models.CASCADE)



