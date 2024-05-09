import cython

# basic arithmetic functions using pure python syntax
# def add(x: cython.double, y: cython.double):
#     return x+y

# def sub(x: cython.double, y: cython.double):
#     return x-y

# def mul(x: cython.double, y: cython.double):
#     return x*y

# def div(x: cython.double, y: cython.double):
#     return x/y

# basic arithmetic functions using cython syntax
def add(double x, double y):
    return x+y

def sub(double x, double y):
    return x-y

def mul(double x, double y):
    return x*y

def div(double x, double y):
    return x/y


# speed comparison of pure python and cython:
def sum_of_first_n_numbers_cythonSyntax(unsigned long long number):
    cdef unsigned long long i = 0
    cdef unsigned long long result = 0
    for i in range(number):
        result += i
    return result

def sum_of_first_n_numbers_purepythonSyntax(number: cython.ulonglong):
    i: cython.ulonglong
    result: cython.ulonglong
    for i in range(number):
        result += i
    return result

# using cdef for function call
# cdef unsigned long long sum_of_first_n_numbers_cythonCdef(unsigned long long number):
#     cdef unsigned long long i = 0
#     cdef unsigned long long result = 0
#     for i in range(number):
#         result += i
#     return result

cdef int sum_of_first_n_numbers_cythonCdef(int number):
    cdef int i = 0
    cdef int result = 0
    for i in range(number):
        result += i
    return result