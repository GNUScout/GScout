# -*- encoding: utf-8 -*-
#!/usr/bin/python

import os
try:
    os.stat("/home/steven/TFG/GScout/document.txt")
    print "Fichero sí existe"
except:
    print "El fichero NO existe"
