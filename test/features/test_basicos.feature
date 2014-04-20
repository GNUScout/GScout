#language: es

    Característica: Comprobar la existencia de ficheros esenciales para ejecutar un proyecto en Django con appengine
      
       Escenario: Comprobar la existencia del fichero manage.py
       Entonces comprobamos la existencia del fichero "manage.py" con la función stat de python
 
       Escenario: Comprobar la existencia del fichero settings.py
       Entonces comprobamos la existencia del fichero "project/settings.py" con la función stat de python


       Escenario: Comprobar la existencia del fichero urls.py del proyecto principal
       Entonces comprobamos la existencia del fichero "project/urls.py" con la función stat de python

       Escenario: Comprobar la existencia del fichero urls.py de la aplicacion socios
       Entonces comprobamos la existencia del fichero "socios/urls.py" con la función stat de python


       Escenario: Comprobar la existencia del fichero Readme
       Entonces comprobamos la existencia del fichero "README.md" con la función stat de python
