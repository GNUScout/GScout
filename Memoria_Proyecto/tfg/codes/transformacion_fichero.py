# Con la llamda a request.FILES['nombre'] se guarda el contenido 
# del fichero en la variable paramFile
paramFile = request.FILES['docfile'].read()

# Con csv.reader(paramFile.splitlines()) dividimos en lineas el 
# contenido del fichero para guardarlo en un array bidimensional 
# compuestos por filas y columnas.
portfolio = csv.reader(paramFile.splitlines())

# Como no nos interesa la primera fila del documento que contiene los 
# nombre de las columnas con el comanto .next() la omitimos.
portfolio.next()