import numpy as np
cimport numpy as cnp
cimport cython

ctypedef cnp.uint64_t DTYPE_UINT64_t# assigns a compile-time type to DTYPE_t

@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function

# This function performs a matrix multiplication for two given matrices: array1 * array2
# TODO accept the raw numpy array and specify dimension and type afterwards
cpdef cnp.ndarray multiply3DmatricesCython(cnp.ndarray[dtype=DTYPE_UINT64_t, ndim=3] arr1, cnp.ndarray[dtype=DTYPE_UINT64_t, ndim=3] arr2):
# cpdef cnp.ndarray multiply3DmatricesCython(np.ndarray array1, np.ndarray array2):

    # print(array1.dtype)
    # print(array2.dtype)
    # cdef cnp.ndarray[dtype=DTYPE_UINT64_t, ndim=3] arr1 = array1.astype(np.uint64)
    # cdef cnp.ndarray[dtype=DTYPE_UINT64_t, ndim=3] arr2 = array2.astype(np.uint64)
    # print(arr1.dtype)
    # print(arr1.dtype)

    cdef int arr1_shape_dim1 = arr1.shape[0]
    cdef int arr1_shape_dim2 = arr1.shape[1]
    cdef int arr1_shape_dim3 = arr1.shape[2]
    cdef int arr2_shape_dim1 = arr2.shape[0]
    cdef int arr2_shape_dim2 = arr2.shape[1]
    cdef int arr2_shape_dim3 = arr2.shape[2]

    # check for dimension errors
    if arr1_shape_dim3 != arr2_shape_dim3:
        print("Dimension error: Third dimension from array1 is " + str(arr1_shape_dim3) + ", and from array2 is " + str(arr2_shape_dim3))
        # TODO handle exception here
    elif arr1_shape_dim2 != arr2_shape_dim1:
        print("Dimension error: dimensions do not match!")
        # TODO handle exception here
    
    # Iterate through third dimension and perform matrix multiplication
    cdef cnp.ndarray returnArray = np.empty([arr1_shape_dim1, arr2_shape_dim2, arr1_shape_dim3])
    cdef int rgbIter = 0
    cdef int rowArr1 = 0
    cdef int columnArr2 = 0
    cdef int columnArr1 = 0
    cdef int currentEntry = 0
    for rgbIter in range(arr1_shape_dim3):
        for rowArr1 in range(arr1_shape_dim2):
            for columnArr2 in range(arr2_shape_dim2):
                currentEntry = 0
                for columnArr1 in range(arr1_shape_dim2):
                    currentEntry += arr1[rowArr1, columnArr1, rgbIter] * arr2[columnArr1, columnArr2, rgbIter]
                returnArray[rowArr1, columnArr2, rgbIter] = currentEntry
    
    return returnArray