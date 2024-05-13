import timeit
import sys
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the working directory to the script directory
os.chdir(script_dir)
sys.path.append(os.path.abspath('cython_module'))
# Append the relative path to the build module
sys.path.append(os.path.join(script_dir, "build", "module"))

import module_name
from module_name import *

import numpy as np
import cv2
import matplotlib.pyplot as plt
import master as mwe
from matrixMultiplication import multiply3DmatricesNumpy
from matrixMultiplication import multiply3DmatricesPython

## Matrix multiplication speed comparison
catImg = cv2.imread('cython_module/pictures/cat_rgb_quadratic_100x100.jpg') 
catImg = cv2.cvtColor(catImg, cv2.COLOR_BGR2RGB) # because cv2 reads images as bgr!
print(str(type(catImg)) + str(catImg.dtype))

catImg = catImg.astype(np.uint64)

numOfExecutions = 1

setupNumpy = '''
import cv2
from matrixMultiplication import multiply3DmatricesNumpy
catImg = cv2.imread('cython_module/pictures/cat_rgb_quadratic_100x100.jpg') 
catImg = cv2.cvtColor(catImg, cv2.COLOR_BGR2RGB)
'''

setupPython = '''
import cv2
from matrixMultiplication import multiply3DmatricesPython
catImg = cv2.imread('cython_module/pictures/cat_rgb_quadratic_100x100.jpg') 
catImg = cv2.cvtColor(catImg, cv2.COLOR_BGR2RGB)
'''

setupCython = '''
import cv2
import master as mwe
catImg = cv2.imread('cython_module/pictures/cat_rgb_quadratic_100x100.jpg') 
catImg = cv2.cvtColor(catImg, cv2.COLOR_BGR2RGB)
'''

setupPybind11 = '''
import cv2
import module_name
from module_name import multiply_3d_arrays_using_stdvector
from module_name import multiply_3d_arrays_using_eigenlibs
catImg = cv2.imread('cython_module/pictures/cat_rgb_quadratic_100x100.jpg') 
catImg = cv2.cvtColor(catImg, cv2.COLOR_BGR2RGB)
'''

numpyTimeMatrixMul = timeit.Timer(lambda: multiply3DmatricesNumpy(catImg, catImg), setup=setupNumpy).timeit(number=numOfExecutions)
pythonTimeMatrixMul = timeit.Timer(lambda: multiply3DmatricesPython(catImg, catImg), setup=setupPython).timeit(number=numOfExecutions)
cythonTimeMatrixMul = timeit.Timer(lambda: mwe.multiply3DmatricesCython(catImg, catImg), setup=setupCython).timeit(number=numOfExecutions)
pybind11TimeMatrixMul_using_stdvector = timeit.Timer(lambda: module_name.multiply_3d_arrays_using_stdvector(catImg, catImg), setup=setupPybind11).timeit(number=numOfExecutions)
pybind11TimeMatrixMul_using_eigenlibs = timeit.Timer(lambda: module_name.multiply_3d_arrays_using_eigenlibs(catImg, catImg), setup=setupPybind11).timeit(number=numOfExecutions)

print("numpyTimeMatrixMul=" + str(numpyTimeMatrixMul))
print("pythonTimeMatrixMul=" + str(pythonTimeMatrixMul))
print("cythonTimeMatrixMul=" + str(cythonTimeMatrixMul))
print("pybind11TimeMatrixMul=" + str(pybind11TimeMatrixMul_using_stdvector))
print("pybind11TimeMatrixMul=" + str(pybind11TimeMatrixMul_using_eigenlibs))
print("Cython is {}x faster than python".format(pythonTimeMatrixMul/cythonTimeMatrixMul))
print("Cython is {}x faster than numpy".format(numpyTimeMatrixMul/cythonTimeMatrixMul))
print("Pybind11 using std::vector is {}x faster than python".format(pythonTimeMatrixMul/pybind11TimeMatrixMul_using_stdvector))
print("Pybind11 using eigen libs is {}x faster than python".format(pythonTimeMatrixMul/pybind11TimeMatrixMul_using_eigenlibs))
print("Pybind11 using eigen libs is {}x faster than numpy".format(numpyTimeMatrixMul/pybind11TimeMatrixMul_using_eigenlibs))

mat_numpy = multiply3DmatricesNumpy(catImg, catImg)
mat_python = multiply3DmatricesNumpy(catImg, catImg)
mat_eiglibs = module_name.multiply_3d_arrays_using_eigenlibs(catImg, catImg)


def show_image(img_array):
    # Convert the NumPy array to uint8
    img_array = np.uint8(img_array)

    # Show the image
    cv2.imshow('Resulting Image', img_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print(mat_numpy.shape)
print(mat_eiglibs.shape)

show_image(catImg)
show_image(mat_numpy)
show_image(mat_eiglibs)

print(np.array_equal(mat_numpy, mat_numpy))
print(np.array_equal(mat_numpy, mat_eiglibs))
print(np.array_equal(mat_numpy, mat_python))