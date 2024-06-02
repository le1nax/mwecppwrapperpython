# distutils: language = c++
# cython: language_level=3

import numpy as np
cimport numpy as cnp
from libc.stdlib cimport malloc, free
from cpython cimport PyCapsule_New, PyCapsule_GetPointer

# Include the Eigen header
cdef extern from "Eigen/Dense" namespace "Eigen":
    cdef cppclass MatrixXd:
        MatrixXd(int, int)
        double& operator()(int, int) except +

    cdef cppclass Map[T]:
        Map(T*, int, int)
        Map(T&)

    ctypedef MatrixXd MapMatrixXd

DTYPE_UINT64_t = np.uint64

cpdef cnp.ndarray multiply3DmatricesCythonUsingEigen(cnp.ndarray[DTYPE_UINT64_t, ndim=3] arr1):
    cdef int rows = arr1.shape[1]
    cdef int cols = arr1.shape[2]
    cdef MapMatrixXd* mat = new MapMatrixXd(<DTYPE_UINT64_t*>arr1.data, rows, cols)

    # Create a result matrix
    cdef MatrixXd result = MatrixXd(rows, cols)

    # Example manipulation: Transpose (as an example)
    result = mat[0].transpose()

    # # Allocate memory for the result NumPy array
    # cdef cnp.ndarray result_np = np.empty((rows, cols), dtype=np.float64)
    # cdef double* result_data = <double*>result_np.data

    # # Copy data from Eigen matrix to NumPy array
    # for i in range(rows):
    #     for j in range(cols):
    #         result_data[i * cols + j] = result(i, j)

    # del mat

    return result_np
