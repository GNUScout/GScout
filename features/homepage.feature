# -*- coding: utf-8 -*-
#language: es

    Característica: Test para comprobar el correcto funcionamiento de la pagina principal 
            
       #los pasos incluidos en el antecedente se ejecutarán antes de cada escenario
       Antecedentes: Ir a la página principal
          Cuando estoy en la página inicial

       Escenario: Comprobando el titulo 
          Entonces compruebo que existe un título y que además es "GSCOUT | ACCESO"
               
                             
       Escenario: Comprobar elementos de la página 
          Entonces busco el elemento "body" y "head"
          Y compruebo que existe un elemento "h2" 
          Y un mensaje de bienvenida
       
       @registro
       Escenario: Registrarse
          Entonces busco el botón "Regístrate!"
          Y compruebo que estoy en la página "/register/"

       @login
       Escenario: Iniciar Sesión
          Entonces busco el botón "Entrar"
          Y compruebo que estoy en la página "/login/"
            
          

