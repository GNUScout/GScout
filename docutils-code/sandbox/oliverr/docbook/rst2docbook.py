#!/usr/bin/env python

# Author: Ollie Rutherfurd
# Contact: oliver@rutherfurd.net
# Revision: $Revision: 3482 $
# Date: $Date: 2005-06-15 23:58:50 +0100 (mié 15 de jun de 2005) $
# Copyright: This module has been placed in the public domain.

"""
A minimal front end to the Docutils Publisher, producing DocBook XML.
"""

import locale
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates DocBook XML documents from standalone reStructuredText '
               'sources.  ' + default_description)

publish_cmdline(writer_name='docbook', description=description)


# :indentSize=4:lineSeparator=\n:noTabs=true:tabSize=4:
