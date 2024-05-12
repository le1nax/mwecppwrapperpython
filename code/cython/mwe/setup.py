# This file acts like a Makefile for python, creating the python module which can be later imported into your python script
# Execute this setup.py by running "python3 setup.py build_ext --inplace"
# Alternatively, if one don't want to run "python3 setup.py build_ext --inplace" every time the .pyx has changed, one can do
# import pyximport; pyximport.install(pyimport=True)
# in the python script

from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

# TODO this is not working!
# extensions = [
#     Extension("*", ["basicArithmetic.pyx", "Multiply_wrapper.pyx"])
# ]

# extensions = [
#     Extension("Multiply_wrapper", ["Multiply_wrapper.pyx"], language="c++")
# ]

# extensions = [
#     Extension("npTest", ["npTest.pyx"],
#               include_dirs=[np.get_include()], language="c++")
# ]

# # This causes two .so to be created and works:
# extensions = [
#     Extension("basicArithmetic", ["basicArithmetic.pyx"]),
#     Extension("Multiply_wrapper", ["Multiply_wrapper.pyx"]),
# ]

# # Include everything - separate .so for every .pyx file will be created:
# extensions = [
#     Extension("*", ["*.pyx"],
#               include_dirs=[np.get_include()],),
# ]

# Include a master file which includes all .pyx files. This generates one module named master:
extensions = [
    Extension("master",# important: module name has to be the same as the .pyx file, otherwise ImportError
              ["master.pyx"],
              include_dirs=[np.get_include()],
              language="c++",),
]

setup(
    name='First cython bindings app',
    ext_modules=cythonize(extensions),
)
