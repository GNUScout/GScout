#!/usr/bin/env python

# Author: Aleksey Gurtovoy
# Contact: agurtovoy@meta-comm.com
# Revision: $Revision: 5203 $
# Date: $Date: 2007-06-04 03:11:15 +0100 (lun 04 de jun de 2007) $
# Copyright: This module has been placed in the public domain.


import locale
try:
    locale.setlocale(locale.LC_ALL, '')
except:
    pass

from docutils.core import publish_cmdline, default_description


description = ('Generates "framed" (X)HTML documents from standalone reStructuredText '
               'sources.  ' + default_description)

publish_cmdline(writer_name='html4_frames', description=description)
