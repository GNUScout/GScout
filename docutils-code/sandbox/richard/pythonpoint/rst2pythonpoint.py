#!/usr/bin/env python

# Author: Lea Wiemann
# Contact: LeWiemann@gmail.com
# Revision: $Revision: 5174 $
# Date: $Date: 2007-05-31 01:01:52 +0100 (jue 31 de may de 2007) $
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing PythonPoint XML.
"""

try:
    import locale
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates PythonPoint documents from standalone reStructuredText '
               'sources.  ' + default_description)

publish_cmdline(writer_name='pythonpoint', description=description)
