import os
import sys

from pprint import pprint
from setuptools import setup, find_packages

sys.dont_write_bytecode = True

setup(
    name="ixpy",
    version='0.0.1',
    description="Python parser for InductEx to interface with the SPiRA framework.",
    author="Ruben van Staden",
    author_email="rubenvanstaden@gmail.com",
    setup_requires=['setuptools-markdown'],
    license="MIT",
    url="https://github.com/rubenvanstaden/spira",

    install_requires=[
        # Basic packages
        'termcolor',
        'colorama',
        'scipy',
        'pytest',
        'numpy',
    ],

    packages=['ixpy'],

    package_dir={'ixpy': 'ixpy'}
)






