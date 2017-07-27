#!/usr/bin/env python

from setuptools import setup

setup(
    name='pyzap',
    version='1.0.0',
    description='Python scraper for accessing ratings from tvbythenumbers.zap2it.com',
    author='sharibarboza',
    author_email='barbozashari@gmail.com',
    url='https://github.com/sharibarboza/pyzap',
    license='MIT License',
    packages=['pyzap'],
    install_requires=[
        'beautifulsoup4',
        'requests>=2.9.1'
    ]
)