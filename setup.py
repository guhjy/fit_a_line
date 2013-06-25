#!/usr/bin/env python
import sys

if 'develop' in sys.argv:
    # use setuptools for develop, but nothing else
    from setuptools import setup
else:
    from distutils.core import setup

with open('README.rst') as file:
    long_description = file.read()

#with open('CHANGES') as file:
#    long_description += file.read()


from fit_a_line import __version__ as version

setup(name='fit_a_line',
      version=version,
      description='Code to fit a simple linear model (which is a surprisingly complicated problem)',
      long_description=long_description,
      author='Adam Ginsburg',
      author_email='adam.ginsburg@colorado.edu',
      data_files=[],
      url='http://github.com/keflavich/fit_a_line',
      packages=['fit_a_line'],
     )
