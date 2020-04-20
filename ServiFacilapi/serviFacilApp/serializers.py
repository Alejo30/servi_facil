from rest_framework import serializers
from pymongo.ssl_support import validate_allow_invalid_certs
from rest_framework.serializers import ALL_FIELDS
from serviFacilApp.models import Persona, Direccion, TipoUser, Usuarios, Empresa, Servicio, Turno


"""Serializadores de ServiFacil"""

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fiels = ALL_FIELDS
        exclude = {}

class TipoUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoUser
        fields = ALL_FIELDS
        exclude = {}
        def create(self, validated_date):
            tipo = TipoUser(**validated_date)
            tipo.save()
            return tipo


class UsuariosSerializer(serializers.ModelSerializer):
    #tipo_usuario = TipoUserSerializer()
    class Meta:
        model = Usuarios
        fields = ALL_FIELDS

        def create(self, validated_data):
            #tipo = validated_data.pop('tipo')
            #tipo_obj = TipoUser(**tipo)
            usuario = Usuarios(**validated_data)
            #usuario.tipo_ususario = tipo_obj
            usuario.save()
            return usuario

class PersonaSerializer(serializers.ModelSerializer):
    #direccion = DireccionSerializer()
    class Meta:
        model = Persona
        fields = ALL_FIELDS

    def create(self, validated_data):
        #direccion = validated_data.pop('direccion')
        #direccion_obj = Direccion(**direccion)
        #usuario = validated_data.pop('usuario')
        #usuario_obj = Usuarios(**usuario)
        persona = Persona(**validated_data)
        #persona.direccion = direccion_obj
        persona.save()
        return persona

    def update(self, instance, validated_data):
        direccion = validated_data.pop('direccion')
        direccion_obj = Direccion(**direccion)
        for key, value in validated_data.items():
            instance.__setattr__(key, value)
            instance.direccion = direccion_obj
            instance.save()
        return instance

    
class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = ALL_FIELDS

    def create(self, validated_data):
        empresa = Empresa(**validated_data)
        #direccion = validated_data.pop('direccion')
        #direccion_obj = Direccion(**direccion)
        #empresa.direccion = direccion_obj
        empresa.save()
        return empresa

    #direccion = DireccionSerializer()


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ALL_FIELDS
    def create(self, validated_data):
        servicio = Servicio(**validated_data)
        servicio.save()
        return servicio
class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ALL_FIELDS
    def create(self, validated_data):
        turno = Turno(**validated_data)
        turno.save()
        return turno

