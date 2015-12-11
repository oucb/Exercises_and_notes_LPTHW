__author__ = 'oucb'

try:
    from setuptools import  setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'ex46',
    version = '0.1',
    packages = ['ex46'],
    scripts = ['bin/ex46_script.py'],
    description = "This is my first project.",
)

