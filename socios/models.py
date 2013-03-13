from django.db import models


class Autorizaciones(models.Model):
    #3 autorizaciones de momento
    autorizacion_medica=models.BooleanField()
    autorizacion_actividades=models.BooleanField()
    autorizacion_fotografias=models.BooleanField()
    
class Familiares(models.Model):
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    nif=models.CharField(max_length=100)
    movil=models.CharField(max_length=100) 
    email=models.CharField(max_length=100)
    profesion=models.CharField(max_length=100)

class Socio(models.Model):
    n_asociado=models.CharField(max_length=100, primary_key=True, unique=True)
    #d_personales=models.ForeignKey(D_Personales, null=True)
    #d_medicos=models.ForeignKey(D_Medicos, null=True)
    #d_economicos=models.ForeignKey(D_Economicos, null=True)
    familiares=models.ForeignKey(Familiares, null=True)
    autorizaciones=models.ForeignKey(Autorizaciones, null=True)     
    
class D_Personales(models.Model):
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    dni=models.CharField(max_length=100)
    sexo=models.BooleanField()
    f_nacimiento=models.DateTimeField()
    direccion=models.CharField(max_length=200)
    c_postal=models.CharField(max_length=100)
    localidad=models.CharField(max_length=100)
    provincia=models.CharField(max_length=100)
    fijo=models.CharField(max_length=100)
    movil=models.CharField(max_length=100)
    f_ingreso=models.DateTimeField()
    f_baja=models.DateTimeField(blank=True, null=True)
    seccion=models.CharField(max_length=100)
    estudios=models.TextField()
    profesion=models.TextField()
    deportes=models.TextField()
    aficiones=models.TextField()
    socio_id=models.ForeignKey(Socio)
    

    
class D_Medicos(models.Model):
    ss=models.CharField(max_length=100)
    smp=models.CharField(max_length=100)
    n_poliza=models.CharField(max_length=100)
    enfermedad=models.CharField(max_length=2)
    t_enfermedad=models.TextField()
    enfermedad_cfp=models.CharField(max_length=2)
    t_enfermedad_cfp=models.TextField()
    operado=models.CharField(max_length=2)
    t_operado=models.TextField()
    alergia=models.CharField(max_length=2)
    t_alergia=models.TextField()
    otras_alergias=models.CharField(max_length=2)
    t_otras_alergias=models.TextField()
    dieta=models.CharField(max_length=2)
    t_dieta=models.TextField()
    toma_medicamentos=models.CharField(max_length=2)
    info_adicional=models.TextField()
    socio_id=models.ForeignKey(Socio)
    
 
class D_Economicos(models.Model):
    titular=models.CharField(max_length=100)
    nif_titular=models.CharField(max_length=100)
    banco=models.CharField(max_length=100)
    sucursal=models.CharField(max_length=100)
    localidad=models.CharField(max_length=100)
    d_banco=models.CharField(max_length=100)
    d_sucursal=models.CharField(max_length=100)
    dc=models.CharField(max_length=100)
    n_cuenta=models.CharField(max_length=100)
    socio_id=models.ForeignKey(Socio)
    



    
class Medicamentos(models.Model):
    nombre=models.CharField(max_length=100)
    dosis=models.CharField(max_length=100)
    pauta=models.CharField(max_length=100)
    socio_id=models.ForeignKey(Socio)    
