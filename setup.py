#!/usr/bin/env python

'''The setup and build script for the octopush library.'''

import os

from setuptools import setup, find_packages

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='octopush',
    version='1.0.0',
    author='Octopush',
    author_email='',
    license='MIT',
    url='https://github.com/bearburger/octopush-api-python',
    keywords='octopush sms',
    description='Python library for Octopush API',
    long_description=(read('README.rst')),
    packages=find_packages(exclude=['tests*']),
    install_requires=['future', 'requests'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
