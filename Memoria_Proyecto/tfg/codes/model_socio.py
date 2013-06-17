from django.db import models
     

class Socio(models.Model):
    n_asociado=models.CharField(max_length=100, primary_key=True, 
                                unique=True)
    alta=models.BooleanField()
    autorizaciones=models.ForeignKey(Autorizaciones, null=True)
    familia_id=models.ForeignKey(Familia,null=True)     
    
class D_Personales(models.Model):
    nombre=models.CharField(max_length=100)
    apellidos=models.CharField(max_length=100)
    dni=models.CharField(max_length=100)
    sexo=models.CharField(max_length=20)
    f_nacimiento=models.DateTimeField()
    direccion=models.CharField(max_length=200)
    c_postal=models.CharField(max_length=100)
    localidad=models.CharField(max_length=100)
    provincia=models.CharField(max_length=100)
    fijo=models.CharField(max_length=100)
    movil=models.CharField(max_length=100)
    f_ingreso=models.DateTimeField(blank=True, null=True)
    f_baja=models.DateTimeField(blank=True, null=True)
    seccion=models.CharField(max_length=100)
    estudios=models.TextField()
    profesion=models.TextField()
    deportes=models.TextField()
    aficiones=models.TextField()
    socio_id=models.ForeignKey(Socio)
        
