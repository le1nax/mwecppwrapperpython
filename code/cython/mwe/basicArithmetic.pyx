# distutils: language = c++
import cython


# basic arithmetic functions using cython syntax
cpdef double add(double x, double y) except *:
    return x+y

cpdef double sub(double x, double y) except *:
    return x-y

cpdef double mul(double x, double y) except *:
    return x*y

cpdef double div(double x, double y) except *:
    return x/y


## speed comparison of pure python and cython:
# cython:
cpdef unsigned long long sum_of_first_n_numbers_cy(unsigned long long number) except *:
    cdef unsigned long long i = 0
    cdef unsigned long long result = 0
    for i in range(number):
        result += i
    return result

# python:
def sum_of_first_n_numbers_py(number):
    result = 0
    for i in range(number):
        result += i
    return result
