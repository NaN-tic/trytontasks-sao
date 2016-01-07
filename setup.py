#!/usr/bin/env python
#This file is part of trytontasks_sao. The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from setuptools import setup, find_packages
import os

execfile(os.path.join('trytontasks_sao', 'version.py'))

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name=PACKAGE,
    version=VERSION,
    description='Tryton Tasks SAO',
    long_description=read('README'),
    author=AUTHOR,
    url=WEBSITE,
    download_url="https://bitbucket.org/trytonspain/trytontasks-modules",
    packages=find_packages(),
    package_data={},
    scripts=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        ],
    license=LICENSE,
    install_requires=[
        'invoke>=0.11.1',
        'blessings',
        ],
    extras_require={},
    zip_safe=False,
    #~ test_suite='trytontasks_sao.tests',
    )
