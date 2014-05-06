# -*- coding: utf-8 -*-
#language: es
   
   Característica: Test para comprobar el correcto funcionamiento de la página de registro
     
     Antecedentes: Ir a la página register
        Dado que estoy en la página "register"
      

     Escenario: Un usuario nuevo desea registrarse
        Entonces compruebo que el contenido de la página es el correcto
        Y relleno los campos para el usuario "test-user"
        Entonces compruebo la existencia del botón "Enviar" y le doy click
        Y se debe mostrar el mensaje "Gracias por registrarte" para finalizar el proceso.
      
