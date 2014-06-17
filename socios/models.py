# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):

    """
      Class for user profile management. 
      This class uses the default :model:`auth.User` django model and returns the user's name.

    """

    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True,help_text="This attribute is optional")
    #picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Autorizaciones(models.Model):

    """Class for authorization management. Authorizations can be: medical, concerning activities undertaken or relevant to the distribution of photographs."""
    
    autorizacion_medica = models.BooleanField()
    autorizacion_actividades = models.BooleanField()
    autorizacion_fotografias = models.BooleanField()
    

class Familia(models.Model):
    """This class is needed to determine which family belongs to a user."""
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nif = models.CharField(max_length=100, primary_key=True, unique=True,help_text="Primary key")
    
    
class Familiares(models.Model):
    """Class managed by the members of a family unit."""
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    nif = models.CharField(max_length=100, primary_key=True, unique=True,help_text="Primary Key")
    telefono = models.CharField(max_length=100)
    movil = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    rol = models.CharField(max_length=100)
    familia_id = models.ForeignKey(Familia, null=True,help_text="foreign key family")
       

class Socio(models.Model):
    """Class for managing partner"""
    n_asociado = models.CharField(max_length=100, primary_key=True, unique=True,help_text="Primary Key")
    alta = models.BooleanField()
    autorizaciones = models.ForeignKey(Autorizaciones, null=True)
    familia_id = models.ForeignKey(Familia, null=True,help_text="foreign key family")
    
class D_Personales(models.Model):
    """class that stores personal data partner"""
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=100)
    sexo = models.CharField(max_length=20)
    f_nacimiento = models.DateTimeField()
    direccion = models.CharField(max_length=200)
    c_postal = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    fijo = models.CharField(max_length=100)
    movil = models.CharField(max_length=100)
    f_ingreso = models.DateTimeField(blank=True, null=True)
    f_baja = models.DateTimeField(blank=True, null=True)
    seccion = models.CharField(max_length=100)
    estudios = models.TextField()
    profesion = models.TextField()
    deportes = models.TextField()
    aficiones = models.TextField()
    socio_id = models.ForeignKey(Socio,help_text="foreign key socio")
    
    
class D_Medicos(models.Model):
    """class medical data managed by partner"""
    c_seguro = models.CharField(max_length=100)
    n_poliza = models.CharField(max_length=100)
    enfermedad = models.CharField(max_length=2, default='no')
    t_enfermedad = models.TextField()
    enfermedad_cfp = models.CharField(max_length=2, default='no')
    t_enfermedad_cfp = models.TextField()
    operado = models.CharField(max_length=2, default='no')
    t_operado = models.TextField()
    alergia = models.CharField(max_length=2, default='no')
    t_alergia = models.TextField()
    otras_alergias = models.CharField(max_length=2, default='no')
    t_otras_alergias = models.TextField()
    dieta = models.CharField(max_length=2, default='no')
    t_dieta = models.TextField()
    toma_medicamentos = models.CharField(max_length=2, default='no')
    info_adicional = models.TextField()
    socio_id = models.ForeignKey(Socio,help_text="foreign key socio")
    
 
class D_Economicos(models.Model):
    """clase que gestiona los datos económicos del socio"""
    titular = models.CharField(max_length=100)
    nif_titular = models.CharField(max_length=100)
    banco = models.CharField(max_length=100)
    sucursal = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    d_banco = models.CharField(max_length=100)
    d_sucursal = models.CharField(max_length=100)
    dc = models.CharField(max_length=100)
    n_cuenta = models.CharField(max_length=100)
    socio_id = models.ForeignKey(Socio,help_text="foreign key socio")
    
    
class Medicamentos(models.Model):
    """Class to add medicines to medical data partner"""
    nombre = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    pauta = models.CharField(max_length=100)
    socio_id = models.ForeignKey(Socio,help_text="foreign key socio")


