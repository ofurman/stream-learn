#! /usr/bin/env python
"""Toolbox for streaming data."""
from __future__ import absolute_import

import codecs
import os
import pypandoc

from setuptools import find_packages, setup

# get __version__ from _version.py
ver_file = os.path.join('strlearn', '_version.py')
with open(ver_file) as f:
    exec(f.read())

DISTNAME = 'stream-learn'
DESCRIPTION = 'Toolbox for streaming data.'
MAINTAINER = 'P. Ksieniewicz'
MAINTAINER_EMAIL = 'pawel.ksieniewicz@pwr.edu.pl'
URL = 'https://github.com/w4k2/stream-learn'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/w4k2/stream-learn'
VERSION = __version__
INSTALL_REQUIRES = ['numpy', 'scipy', 'scikit-learn', 'liac-arff','scikit-learn','tqdm','future']


setup(name=DISTNAME,
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      description=DESCRIPTION,
      long_description=pypandoc.convert('README.md', 'rst'),
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      packages=find_packages(),
      install_requires=INSTALL_REQUIRES)
