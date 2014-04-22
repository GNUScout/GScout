#language: es

    Característica: Test para comprobar el correcto funcionamiento de la pagina principal 
       
       #@browser     
       Escenario: Comprobando el titulo
          Cuando voy a la página inicial
          Entonces compruebo que existe un titulo y que ademas es "GSCOUT | ACCESO"
               
       #@browser                               
       Escenario: Comprobar elementos de la pagina
          Cuando voy a la página inicial 
          Entonces busco el elemento "body" y "head"



