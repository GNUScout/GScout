# -*- coding: utf-8 -*-
#language: es

   Característica: Test para comprobar el correcto funcionamiento de la página de login
     
     Antecedentes: Ir a la página para acceder a la cuenta de usuario
        #paso heredado de register.feature
        Dado que estoy en la página "login" 
      

     Escenario: Un usuario desea acceder a su cuenta
        Entonces relleno los campos para el usuario "steven2"
        #paso heredado de register.feature
        Entonces compruebo la existencia del botón "Acceder" y le doy click 
        Y debo estar en la página "socios" 

