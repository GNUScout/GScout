#! /usr/bin/env python

# $Id: test_functions.py 6495 2010-12-07 10:42:53Z milde $
# Author: David Goodger <goodger@python.org>
# Copyright: This module has been placed in the public domain.

"""
Tests for PySource Reader functions.
"""

import unittest
from __init__ import DocutilsTestSupport
from docutils.readers.python.moduleparser import trim_docstring


class MiscTests(unittest.TestCase):

    docstrings = (
        ("""""", """"""), # empty
        ("""Begins on the first line.

        Middle line indented.

    Last line unindented.
    """,
         """\
Begins on the first line.

    Middle line indented.

Last line unindented."""),
        ("""
    Begins on the second line.

        Middle line indented.

    Last line unindented.""",
         """\
Begins on the second line.

    Middle line indented.

Last line unindented."""),
        ("""All on one line.""", """All on one line."""))

    def test_trim_docstring(self):
        for docstring, expected in self.docstrings:
            self.assertEquals(trim_docstring(docstring), expected)
            self.assertEquals(trim_docstring('\n    ' + docstring),
                              expected)


if __name__ == '__main__':
    unittest.main()
