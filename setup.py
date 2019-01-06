#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from setuptools import (
    setup,
    find_packages,
)

extras_require={
    'test': [
        "pytest>=3.6.0",
        "tox>=2.9.1,<3",
    ],
    'lint': [
        "flake8==3.4.1",
        "isort>=4.2.15,<5",
    ],
    'doc': [
        "Sphinx>=1.6.5,<2",
        "sphinx_rtd_theme>=0.1.9",
    ],
    'dev': [
        "bumpversion>=0.5.3,<1",
        "pytest-xdist",
        "pytest-watch>=4.1.0,<5",
        "wheel",
        "ipython",
    ],
}

extras_require['dev'] = (
    extras_require['dev']
    + extras_require['test']
    + extras_require['lint']
    + extras_require['doc']
)

install_requires = [
    'web3>=5.0.0a1,<6.0.0',
]
if sys.platform == 'win32':
    install_requires.append('pypiwin32')

setup(
    name='ethtoken',
    # NOTE: do not change version manually, use `make release bump=$$PART_TO_BUMP$$` instead
    version='0.0.1-alpha.4',
    description="""Ethereum EIP20 Token Interface""",
    long_description_markdown_filename='README.md',
    author='Jason Carver',
    author_email='ut96caarrs@snkmail.com',
    url='https://github.com/carver/ethtoken.py',
    include_package_data=True,
    install_requires=install_requires,
    setup_requires=['setuptools-markdown'],
    extras_require=extras_require,
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
        'Programming Language :: Python :: 3.6',
    ],
)
