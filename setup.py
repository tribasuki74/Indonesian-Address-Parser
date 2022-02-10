#!/usr/bin/env python
import os
from setuptools import find_packages, setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Indonesian_Address_Parser",
    version="0.0.1",
    description='Python library for Game Guesser',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/tribasuki74/Indonesian-Address-Parser',
    download_url='https://github.com/tribasuki74/Indonesian-Address-Parser/archive/v0.0.1.tar.gz',    
    author="Tri Basuki Kurniawan",
    author_email='tribasuki@thelorry.com',
    packages=["Indonesian_Address_Parser", "database"],
    license='MIT',
    install_requires=[],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',
    ]
)