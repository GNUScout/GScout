#!/usr/bin/env python

# Author: Ollie Rutherfurd
# Contact: oliver@rutherfurd.net
# Revision: $Revision: 3483 $
# Date: $Date: 2005-06-16 00:06:27 +0100 (jue 16 de jun de 2005) $
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing an .ht 
(HTML Template) file.
"""

import locale
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates .ht (HTML Template) documents from standalone reStructuredText '
               'sources.  ' + default_description)

publish_cmdline(writer_name='hthtml', description=description)


# :indentSize=4:lineSeparator=\n:noTabs=true:tabSize=4:
