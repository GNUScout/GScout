#!/bin/bash
# Borra los reportes existentes y crea de nuevo la carpeta vacia
rm -rf pymetrics/
mkdir pymetrics
rm -rf pylint/
mkdir pylint

# Indicadores para el Modulo Socio
echo "Generating metrics for User module..."
pymetrics -i simple:SimpleMetric,mccabe:McCabeMetric 
	     socios/views.py socios/models.py > pymetrics/Socios.txt
pylint -d C0103,E1101,C0301 -f html socios/ > pylint/Socios.html

# Borra los archivos temporales
echo "Cleaning temp files..."
rm -f metricData.*
