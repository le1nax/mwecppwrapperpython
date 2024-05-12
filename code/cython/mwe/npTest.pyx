import numpy as np
cimport numpy as cnp
cimport cython

ctypedef cnp.int_t DTYPE_INT_t# assigns a compile-time type to DTYPE_t

@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
cpdef cnp.ndarray add_numpy_elements(cnp.ndarray[dtype=DTYPE_INT_t, ndim=2] arr):
    cdef unsigned long long int total = 0# initialisation important here!
    cdef int k
    cdef int i
    cdef int arr_shape_dim0 = arr.shape[0]
    cdef int arr_shape_dim1 = arr.shape[1]
    cdef cnp.ndarray returnArray = np.empty([1,3])

    print(arr)

    # print("First dimension=" + str(arr_shape_dim0))
    # print("Second dimension=" + str(arr_shape_dim1))

    # iterate through array
    for k in range(arr_shape_dim1):
        total = total + arr[0,k]# important for speed: indexing instead of iterating
        print("arr[arr_shape_dim0,k]=" + str(arr[0,k]))
        print("total=" + str(total))
    
    # generate new cnp array and return it as a numpy array
    for i in range(arr_shape_dim1):
        returnArray[0,i] = arr[0,i] + i
        print("returnArray[arr_shape_dim0,i]=" + str(returnArray[0,i]))
    
    return returnArray