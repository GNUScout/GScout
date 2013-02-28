from django.db import models

class D_Personales(models.Model):
    nombre=models.CharField()
    apellidos=models.CharField()
    dni=models.CharField()
    f_nacimiento=models.DateTimeField()
    direccion=models.TextField()
    c_postal=models.CharField()
    Localidad=models.CharField()
    Provincia=models.CharField()
    fijo=models.CharField()
    movil=models.CharField()
    f_ingreso=models.CharField()
    f_baja=models.CharField()
    seccion=models.CharField()
    estudios=models.TextField()
    profesion=models.TextField()
    deportes=models.TextField()
    aficciones=models.TextField()
    
class Medicamentos(models.Model):
    nombre=models.CharField()
    dosis=models.CharField()
    pauta=models.CharField()
        
    
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
    titular=models.CharField()
    NIF_titular=models.CharField()
    Banco=models.CharField()
    Sucursal=models.CharField()
    Localidad=models.CharField()
    d_banco=models.CharField()
    d_sucursal=models.CharField()
    dc=models.CharField()
    n_cuenta=models.CharField()
    
class Autorizaciones(models.Model):
    #3 autorizaciones de momento
    autorizacion_medica=models.BooleanField()
    autorizacion_actividades=models.BooleanField()
    autorizacion_fotografias=models.BooleanField()
    
class Familiares(models.Model):
    nombre=models.CharField()
    apellidos=models.CharField()
    NIF=models.CharField()
    movil=models.CharField() 
    email=models.CharField()
    profesion=models.CharField()

class Socio(models.Model):
    n_asociado=models.CharField()
    d_personales=models.ForeignKey(D_Personales, null=True)
    d_medicos=models.ForeignKey(D_Medicos, null=True)
    d_personales=models.ForeignKey(D_Economicos, null=True)
    familiares=models.ForeignKey(Familiares, null=True)
    autorizaciones=models.ForeignKey(Autorizaciones, null=True)     