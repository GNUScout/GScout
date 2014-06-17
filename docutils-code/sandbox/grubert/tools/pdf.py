#!/usr/bin/env python

"""
:Author: Engelbert Gruber
:Contact: grubert@users.sourceforge.net
:Revision: $Revision: 826 $
:Date: $Date: 2002-10-18 06:10:33 +0100 (vie 18 de oct de 2002) $
:Copyright: This module has been placed in the public domain.

A minimal front-end to the Docutils Publisher, producing PDF via ReportLabs.
"""

from docutils.core import publish_cmdline
try:
    from docutils.writers.rlpdf import Writer
except ImportError:
    from rlpdf import Writer


usage = 'usage:\n  %prog [options] [source [destination]]'

publish_cmdline(writer=Writer(), usage=usage)
