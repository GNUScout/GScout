#!/usr/bin/env python

# Author: Lalo Martins
# Contact: lalo@laranja.org
# Revision: $Revision: 1749 $
# Date: $Date: 2003-11-29 05:02:51 +0000 (sáb 29 de nov de 2003) $
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing Lout.
"""

import locale
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates Lout documents from standalone reStructuredText '
			   'sources.  ' + default_description)

publish_cmdline(writer_name='lout', description=description)
