# Generated by Django 2.2.11 on 2020-04-06 03:43

from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields
import serviFacilApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle_principal', models.CharField(max_length=120)),
                ('calle_secundaria', models.CharField(max_length=120)),
                ('numero_local', models.CharField(default='S/N', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=20, unique=True)),
                ('nombres', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('telefono', models.IntegerField()),
                ('direccion', djongo.models.fields.EmbeddedField(model_container=serviFacilApp.models.Direccion, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10, unique=True)),
                ('Descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='serviFacilApp.Persona')),
                ('tipo_ususario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='serviFacilApp.TipoUser')),
            ],
        ),
    ]
