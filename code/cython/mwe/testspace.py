import timeit
import numpy as np
# import pyximport; pyximport.install(pyimport=True)
import cv2
import matplotlib.pyplot as plt
import master as mwe
from matrixMultiplication import *

# add_result = mwe.add(2,3)
# print(str(add_result) + str(type(add_result)))

# ## speed comparison between pure python loops and with typeinformation using cython
# pythonTime = timeit.timeit('master.sum_of_first_n_numbers_py(1000)', setup='import master', number=100)
# cythonTime = timeit.timeit('master.sum_of_first_n_numbers_cy(1000)', setup='import master', number=100)

# print("pythonTime=" + str(pythonTime))
# print("cythonTime=" + str(cythonTime))
# print("Cython is {}x faster".format(pythonTime/cythonTime))

# ## C++ class API test
# multiply_obj = mwe.PyMultiply(1.5, 3)
# multiply_obj = mwe.PyMultiply(1.5, 3)
# print(multiply_obj.getFactors())
# print(multiply_obj.multiply())
# print(dir(multiply_obj))

# ## Testing numpy interface
# newArray = mwe.add_numpy_elements(np.array([[1, 2, 3]]))
# print(str(newArray) + ", type=" + str(type(newArray)))

## Matrix multiplication speed comparison
catImg = cv2.imread('/Users/matthi/Documents/Elektrotechnik_Studium/Studium/Master/ss24/Seminar_PyPlusPlus/mwecppwrapperpython/code/cython/mwe/pictures/cat_rgb.jpg') 
catImg = cv2.cvtColor(catImg, cv2.COLOR_BGR2RGB) # because cv2 reads images as bgr!
print(type(catImg))

pythonTimeMatrixMul = timeit.timeit('multiply3Dmatrices(catImg, catImg)', setup='matrixMultiplication import *', number=1)
cythonTimeMatrixMul = timeit.timeit('master.multiply3Dmatrices(catImg, catImg)', setup='import master', number=1)
# pybind11TimeMatrixMul = timeit.timeit('<TODO>', setup='import <name of module>', number=1)

print("pythonTimeMatrixMul=" + str(pythonTimeMatrixMul))
print("cythonTimeMatrixMul=" + str(cythonTimeMatrixMul))
# print("pybind11TimeMatrixMul=" + str(pybind11TimeMatrixMul))
print("Cython is {}x faster than python".format(pythonTimeMatrixMul/cythonTimeMatrixMul))
# print("Pybind11 is {}x faster than python".format(pythonTimeMatrixMul/pybind11TimeMatrixMul))