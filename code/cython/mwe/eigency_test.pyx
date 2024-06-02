from eigency.core cimport *
cimport numpy as cnp

cdef extern from "eigency_test.hpp":
     cdef void _printEigenMatrix "printEigenMatrix"(FlattenedMap[Matrix, float, Dynamic, Dynamic] &)

# This will be exposed to Python
def printEigenMatrix(np.ndarray[np.float64_t, ndim=2] array):
    return _printEigenMatrix(FlattenedMap[Matrix, float, Dynamic, Dynamic](array))