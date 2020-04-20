from django import forms
from .models import Persona, Usuarios, Empresa, Servicio, Turno


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = [
            'cedula',
            'nombres',
            'apellidos',
            'correo',
            #'fecha_nacimiento',
            #'telefono',
            #'direccion',
        ]

        labels = {
            'cedula': 'Cedula',
            'nombres': 'Nombres',
            'apellidos': 'Apellidos',
            'correo': 'Correo Electronico',
            #'fecha_nacimiento': 'Fecha Nacimiento',
            #'telefono': 'Telefono',
            #'direccion': 'Direccion',
        }

        widgets = {
            'cedula': forms.TextInput(attrs={'class':'form-control'}),
            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            #'fecha_nacimiento': forms.DateInput(attrs={'class':'form-control'}),
            #'telefono': forms.TextInput(attrs={'class':'form-control'}),
            #'direccion': forms.EmbeddedField(attrs={'class':'form-control'}),
        }

class DireccionForm(forms.ModelForm):
    fields = [
        'calle_principal',
        'calle_secundaria',
        'numero_local',
    ]
    labels = {
        'calle_principal': 'Calle Principal',
        'calle_secundaria': 'Calle Secundaria',
        'numero_local': 'Numero',

    }
    widgets = {
        'calle_principal': forms.TextInput(attrs={'class':'form-control'}),
        'calle_secundaria': forms.TextInput(attrs={'class':'form-control'}),
        'numero_local': forms.TextInput(attrs={'class':'form-control'}),
    }

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa

        fields = [
            'nombre',
            'ruc',
            'direccion',
            'persona',
        ]
        labels = {
            'nombre': 'Nombre',
            'ruc': 'RUC',
            'direccion': 'Direccion',
            'persona': 'Persona',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'ruc': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
        }

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = [
            'nombre',
            'descripcion',
            'empresa',
        ]
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripcion',
            'empresa': 'Empresa',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'empresa': forms.Select(attrs={'class':'form-control'}),
        }
class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = [
            'fecha',
            'hora',
            'descripcion',
            'persona',
            'empresa',
            'servicio',
        ]
        labels = {
            'fecha': 'Fecha',
            'hora': 'Hora',
            'descripcion': 'Descripcion',
            'persona': 'Persona',
            'empresa': 'Empresa',
            'servicio':'Servicio',
        }
        widgets = {
            'fecha': forms.DateInput(attrs={'class':'form-control'}),
            'hora': forms.TimeInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'persona': forms.Select(attrs={'class':'form-control'}),
            'empresa': forms.Select(attrs={'class':'form-control'}),
            'servicio': forms.Select(attrs={'class':'form-control'}),
        }
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = [
            'username',
            'password',
            'tipo_ususario',
        ]

        labels = {
            'username': 'Username',
            'password': 'Password',
            'tipo_ususario': 'Tipo de Usuario',
        }

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_ususario': forms.Select(attrs={'class':'form-control'}),
        }