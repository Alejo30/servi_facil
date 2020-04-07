from rest_framework import serializers
from rest_framework.serializers import ALL_FIELDS
from .models import Persona, Direccion, TipoUser, Usuarios


"""Serializadores de ServiFacil"""

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fiels = ALL_FIELDS


class PersonaSerializer(serializers.ModelSerializer):
    direccion = DireccionSerializer()
    class Meta:
        model = Persona
        fields = ALL_FIELDS

    def create (self, validated_data):
        print('Todo')
        return None

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ALL_FIELDS
    

