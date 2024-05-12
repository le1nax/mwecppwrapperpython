import numpy as np
cimport numpy as cnp
# This includes the Multiply.cpp
# Alternatively, add the expression in brackets to the top of the .pyx file: (# distutils: sources = Rectangle.cpp)
cdef extern from "Multiply.cpp":# path relative to the setup.py file
    pass

# This declares the public functions and attributes of the class to cython
cdef extern from "Multiply.hpp" namespace "math":
    cdef cppclass Multiply:
        Multiply() except +# except + necessary to rise a python exception when initial memory allocation rises an exception
        Multiply(double factor1, double factor2) except +

        double getFactor1()
        double getFactor2()
        void setFactors(double factor1, double factor2)
        # cnp.ndarray getFactors()
        double multiply(double factor1, double factor2)
        double multiply()