#!/usr/bin/env python

# Author: David Goodger
# Contact: goodger@users.sourceforge.net
# Revision: $Revision: 1174 $
# Date: $Date: 2003-02-13 16:12:51 +0000 (jue 13 de feb de 2003) $
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing pseudo-XML.
"""

import locale
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish, default_description

import OOdirectives


description = ('Generates pseudo-XML from standalone reStructuredText '
               'sources (for testing purposes).  ' + default_description)

publish(description=description)
