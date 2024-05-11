# distutils: language = c++

from Multiply cimport Multiply

# Create a Cython extension type which holds a C++ instance
# as an attribute and create a bunch of forwarding methods
# Python extension type.
cdef class PyMultiply:
    cdef Multiply multiply_inst  # Hold a C++ instance which we're wrapping

    def __init__(self, double factor1, double factor2):
        self.multiply_inst = Multiply(factor1, factor2)

    def getFactor1(self):
        return self.multiply_inst.getFactor1()
    
    def getFactor2(self):
        return self.multiply_inst.getFactor2()
    
    def setFactors(self, factor1, factor2):
        return self.multiply_inst.setFactors(factor1, factor2)

    def multiply(self, factor1, factor2):
        return self.multiply_inst.multiply(factor1, factor2)

    def multiply(self):
        return self.multiply_inst.multiply()