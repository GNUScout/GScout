# language: es

   Característica: Comprobar la existencia de ficheros esenciales para ejecutar un proyecto en Django con appengine
       Escenario: Comprobar la existencia del fichero urls.py
          Entonces comprobamos la existencia del fichero "urls.py" con la función stat de python
       
       Escenario: Comprobar la existencia del fichero settings.py
          Entonces comprobamos la existencia del fichero "settings.py" con la función stat de python

       Escenario: Comprobar la existencia del fichero de configuración app.yaml para appengine
          Entonces comprobamos la existencia del fichero "app.yaml" con la función stat de python
