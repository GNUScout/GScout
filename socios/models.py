from django.db import models

class D_Personales(models.Model):
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    dni=models.CharField(max_length=100)
    f_nacimiento=models.DateTimeField()
    direccion=models.TextField()
    c_postal=models.CharField(max_length=100)
    Localidad=models.CharField(max_length=100)
    Provincia=models.CharField(max_length=100)
    fijo=models.CharField(max_length=100)
    movil=models.CharField(max_length=100)
    f_ingreso=models.CharField(max_length=100)
    f_baja=models.CharField(max_length=100)
    seccion=models.CharField(max_length=100)
    estudios=models.TextField()
    profesion=models.TextField()
    deportes=models.TextField()
    aficciones=models.TextField()
    
class Medicamentos(models.Model):
    nombre=models.CharField(max_length=100)
    dosis=models.CharField(max_length=100)
    pauta=models.CharField(max_length=100)
        
    
class D_Medicos(models.Model):
    seguro= (
             ('ss', 'Seguridad Social'),
             ('smp', 'Seguro Medico Privado'),
             )
    enfermedad=models.BooleanField()
    t_enfermedad=models.TextField()
    enfermedad_cfp=models.BooleanField()
    t_enfermedad_cfp=models.TextField()
    operado=models.BooleanField()
    t_operado=models.TextField()
    alergia_medicamento=models.BooleanField()
    t_alergia_medicamento=models.TextField()
    otras_alergias=models.BooleanField()
    t_otras_alergias=models.TextField()
    toma_medicamentos=models.BooleanField()
    medicamentos=models.ForeignKey(Medicamentos)
    info_adicional=models.TextField()
    
 
class D_Economicos(models.Model):
    titular=models.CharField(max_length=100)
    NIF_titular=models.CharField(max_length=100)
    Banco=models.CharField(max_length=100)
    Sucursal=models.CharField(max_length=100)
    Localidad=models.CharField(max_length=100)
    d_banco=models.CharField(max_length=100)
    d_sucursal=models.CharField(max_length=100)
    dc=models.CharField(max_length=100)
    n_cuenta=models.CharField(max_length=100)
    
class Autorizaciones(models.Model):
    #3 autorizaciones de momento
    autorizacion_medica=models.BooleanField()
    autorizacion_actividades=models.BooleanField()
    autorizacion_fotografias=models.BooleanField()
    
class Familiares(models.Model):
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    NIF=models.CharField(max_length=100)
    movil=models.CharField(max_length=100) 
    email=models.CharField(max_length=100)
    profesion=models.CharField(max_length=100)

class Socio(models.Model):
    n_asociado=models.CharField(max_length=100)
    d_personales=models.ForeignKey(D_Personales, null=True)
    d_medicos=models.ForeignKey(D_Medicos, null=True)
    d_personales=models.ForeignKey(D_Economicos, null=True)
    familiares=models.ForeignKey(Familiares, null=True)
    autorizaciones=models.ForeignKey(Autorizaciones, null=True)     