#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from setuptools import (
    setup,
    find_packages,
)


DIR = os.path.dirname(os.path.abspath(__file__))

install_requires = [
    'web3~=4.0b',
]
if sys.platform == 'win32':
    install_requires.append('pypiwin32')

setup(
    name='ethtoken',
    version='0.0.1a1',
    description="""Ethereum EIP20 Token Interface""",
    long_description_markdown_filename='README.md',
    author='Jason Carver',
    author_email='ut96caarrs@snkmail.com',
    url='https://github.com/carver/ethtoken.py',
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=['setuptools-markdown'],
    py_modules=['ethtoken'],
    license="MIT",
    zip_safe=False,
    keywords='ethereum erc20 token eip20 ICO ETH',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
