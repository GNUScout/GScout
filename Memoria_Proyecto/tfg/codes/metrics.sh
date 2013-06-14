#!/bin/bash

# Cleaning existing reports and creating the folder
rm -rf pymetrics/
mkdir pymetrics
rm -rf pylint/
mkdir pylint

# Metrics for socios module
echo "Generating metrics for User module..."
pymetrics -i simple:SimpleMetric,mccabe:McCabeMetric 
	     socios/views.py socios/models.py > pymetrics/Socios.txt
pylint -d C0103,E1101,C0301 -f html socios/ > pylint/Socios.html

# Cleaning temp files...
echo "Cleaning temp files..."
rm -f metricData.*
