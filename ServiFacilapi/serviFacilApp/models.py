from djongo import models
from django import forms
# Create your models here.

class Direccion(models.Model):
    calle_principal = models.CharField(max_length=120)
    calle_secundaria = models.CharField(max_length=120)
    numero_local = models.CharField(max_length=120, default='S/N')


class Persona(models.Model):
    cedula = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    telefono = models.IntegerField()
    direccion = models.EmbeddedField(
        model_container=Direccion
    )

class TipoUser(models.Model):
    nombre = models.CharField(max_length=10, unique=True)
    Descripcion = models.CharField(max_length=150)


class Usuarios(models.Model):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=20)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE,
                                   null=False, blank=False)
    tipo_ususario = models.OneToOneField(TipoUser, on_delete=models.CASCADE,
                                   null=False, blank=False)




