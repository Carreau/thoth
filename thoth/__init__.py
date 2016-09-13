"""
A declarative way of invoking sphinx, 

And writing the configuration in pyproject.toml

This module is more opinionated than sphinx.
"""

__version__ = '0.0.1'

from sphinx import cmdline
from sphinx.application import Sphinx

import os
import os.path




def main():
    print('sphinx-build -b html -d _build/doctrees . _build/html')
    cmdline.main('sphinx-build -b html -d _build/doctrees . _build/html'.split(' '))
    here = os.getcwd()
    srcdir = here
    confdir = os.path.join(here,'docs')
    confdir = None
    outdir = os.path.join(here,'_build/html/{version}'.format(version='X.y.z'))
    doctreedir = os.path.join(here,'.cache')

    builder = Sphinx(srcdir, confdir, outdir, doctreedir, 'html', confoverrides={'master_doc':'index'})
    builder.build(None, [])
    print('it works')
