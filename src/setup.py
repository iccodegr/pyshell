#!/usr/bin/env python
from setuptools import setup

setup(
    name='pyshell',
    version='0.5',
    description='web bashed python shell',
    author='Tasos Vogiatzoglou',
    author_email='tvoglou@iccode.gr',
    packages=['pyshell','pyshell.jedi'],
    package_dir={
        'pyshell':'pyshell',
        'pyshell.jedi':'pyshell/jedi',
        'pyshell.frontend':'pyshell/frontend'
    },
    package_data={
        'pyshell':['frontend/**/*.*']
    },
    requires=[
        'CherryPy'
    ]
)
