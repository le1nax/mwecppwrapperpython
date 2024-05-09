from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Basic arithmetic app',
    ext_modules=cythonize("basic_arithmetic.pyx"),
)