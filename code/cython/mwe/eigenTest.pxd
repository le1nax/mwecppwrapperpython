cimport numpy as cnp

# Declare the Eigen types we will use
cdef extern from "Eigen/Dense" namespace "Eigen":
    cdef cppclass MatrixXd:
        MatrixXd(int, int)
        double& operator()(int, int) except +

    cdef cppclass Map[T]:
        Map(T*, int, int)
        Map(T&)

    ctypedef MatrixXd MapMatrixXd