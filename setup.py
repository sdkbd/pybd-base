# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.2'


setup(
    name='pybd-base',
    version=version,
    keywords='Baidu XiongZhang Base Class',
    description='Baidu XiongZhang Base Class for Python.',
    long_description=open('README.rst').read(),

    url='https://github.com/sdkbd/pybd-base',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['pybd_base'],
    py_modules=[],
    install_requires=['pywe-xml', 'requests'],

    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
