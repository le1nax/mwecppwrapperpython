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

# Read an image as test matrix
catImg = cv2.imread('cython_module/pictures/cat_rgb_quadratic_100x100.jpg') 
catImg = cv2.cvtColor(catImg, cv2.COLOR_BGR2RGB) # because cv2 reads images as bgr!
print("type(catImg)=" + str(type(catImg)) + ", catImg.dtype=" + str(catImg.dtype))
# print("originalImg_1=" + str(catImg[:,:,0]))
# print("originalImg_2=" + str(catImg[:,:,1]))
# print("originalImg_3=" + str(catImg[:,:,2]))
# print("originalImgOrderingCmajor=" + str(catImg.flags['C_CONTIGUOUS']))
catImg = np.ascontiguousarray(catImg)# ensure that we have a row_major order

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
# Record the time for some python->C++ matrix multiplication implementations
numpyTimeMatrixMul = timeit.Timer(lambda: multiply3DmatricesNumpy(catImg, catImg), setup=setupNumpy).timeit(number=numOfExecutions)
pythonTimeMatrixMul = timeit.Timer(lambda: multiply3DmatricesPython(catImg, catImg), setup=setupPython).timeit(number=numOfExecutions)
cythonTimeMatrixMul = timeit.Timer(lambda: mwe.multiply3DmatricesCython(catImg, catImg), setup=setupCython).timeit(number=numOfExecutions)
pybind11TimeMatrixMul_using_stdvector = timeit.Timer(lambda: module_name.multiply_3d_arrays_using_stdvector(catImg, catImg), setup=setupPybind11).timeit(number=numOfExecutions)
pybind11TimeMatrixMul_using_eigenlibs = timeit.Timer(lambda: module_name.multiply_3d_arrays_using_eigenlibs(np.transpose(catImg, (2, 0, 1)), np.transpose(catImg, (2, 0, 1))), setup=setupPybind11).timeit(number=numOfExecutions)

print("numpyTimeMatrixMul=" + str(numpyTimeMatrixMul))
print("pythonTimeMatrixMul=" + str(pythonTimeMatrixMul))
print("cythonTimeMatrixMul=" + str(cythonTimeMatrixMul))
print("pybind11TimeMatrixMulstdVector=" + str(pybind11TimeMatrixMul_using_stdvector))
print("pybind11TimeMatrixMulEigen=" + str(pybind11TimeMatrixMul_using_eigenlibs))
print("Cython is {}x faster than python".format(pythonTimeMatrixMul/cythonTimeMatrixMul))
print("Cython is {}x faster than numpy".format(numpyTimeMatrixMul/cythonTimeMatrixMul))
print("Pybind11 using std::vector is {}x faster than python".format(pythonTimeMatrixMul/pybind11TimeMatrixMul_using_stdvector))
print("Pybind11 using eigen libs is {}x faster than python".format(pythonTimeMatrixMul/pybind11TimeMatrixMul_using_eigenlibs))
print("Pybind11 using eigen libs is {}x faster than numpy".format(numpyTimeMatrixMul/pybind11TimeMatrixMul_using_eigenlibs))

mat_purePython = multiply3DmatricesPython(catImg, catImg)
mat_pureNumpy = multiply3DmatricesNumpy(catImg, catImg)
mat_cython = mwe.multiply3DmatricesCython(catImg, catImg)
mat_pybind11_stdVector = module_name.multiply_3d_arrays_using_stdvector(catImg, catImg)
mat_pybind11_eiglibs = module_name.multiply_3d_arrays_using_eigenlibs(np.transpose(catImg, (2, 0, 1)), np.transpose(catImg, (2, 0, 1)))
print("mat_eiglibs order row major? =" + str(mat_pybind11_eiglibs.flags['C_CONTIGUOUS']))

def show_image(img_array):
    # Convert the NumPy array to uint8
    img_array = np.uint8(img_array)

    # Show the image
    cv2.imshow('Resulting Image', img_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("mat_numpy.shape=" + str(mat_pureNumpy.shape))
print("mat_eiglibs.shape=" + str(mat_pybind11_eiglibs.shape))

# Show the images
show_image(catImg)
show_image(mat_purePython)
show_image(mat_pureNumpy)
show_image(mat_cython)
show_image(mat_pybind11_stdVector)
show_image(np.transpose(mat_pybind11_eiglibs, (1, 2, 0)))

# Check if images are equal
print(np.array_equal(mat_pureNumpy, mat_pureNumpy))
print(np.array_equal(mat_pureNumpy, mat_purePython))
print(np.array_equal(mat_pureNumpy, mat_cython))
print(np.array_equal(mat_pureNumpy, mat_pybind11_stdVector))
print(np.array_equal(mat_pureNumpy, mat_pybind11_eiglibs))

