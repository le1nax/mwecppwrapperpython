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
catImg = cv2.imread('cython_module/pictures/cat_rgb_quadratic_2x2.jpg') 
catImg = cv2.cvtColor(catImg, cv2.COLOR_BGR2RGB) # because cv2 reads images as bgr!
print("type(catImg)=" + str(type(catImg)) + ", catImg.dtype=" + str(catImg.dtype))
# print(catImg)
# print(catImg[:,:,0])
# print(catImg[:,:,1])
# print(catImg[:,:,2])
print("originalImg_1=" + str(catImg[:,:,0]))
print("originalImg_2=" + str(catImg[:,:,1]))
print("originalImg_3=" + str(catImg[:,:,2]))
print("originalImgOrderingCmajor=" + str(catImg.flags['C_CONTIGUOUS']))
catImg = np.ascontiguousarray(catImg)

catImg = catImg.astype(np.uint64)

numOfExecutions = 1

setupNumpy = '''
import cv2
from matrixMultiplication import multiply3DmatricesNumpy
catImg = cv2.imread('cython_module/pictures/cat_rgb_quadratic_2x2.jpg') 
catImg = cv2.cvtColor(catImg, cv2.COLOR_BGR2RGB)
'''

setupPython = '''
import cv2
from matrixMultiplication import multiply3DmatricesPython
catImg = cv2.imread('cython_module/pictures/cat_rgb_quadratic_2x2.jpg') 
catImg = cv2.cvtColor(catImg, cv2.COLOR_BGR2RGB)
'''

setupCython = '''
import cv2
import master as mwe
catImg = cv2.imread('cython_module/pictures/cat_rgb_quadratic_2x2.jpg') 
catImg = cv2.cvtColor(catImg, cv2.COLOR_BGR2RGB)
'''

setupPybind11 = '''
import cv2
import module_name
from module_name import multiply_3d_arrays_using_stdvector
from module_name import multiply_3d_arrays_using_eigenlibs
catImg = cv2.imread('cython_module/pictures/cat_rgb_quadratic_2x2.jpg') 
catImg = cv2.cvtColor(catImg, cv2.COLOR_BGR2RGB)
'''

numpyTimeMatrixMul = timeit.Timer(lambda: multiply3DmatricesNumpy(catImg, catImg), setup=setupNumpy).timeit(number=numOfExecutions)
pythonTimeMatrixMul = timeit.Timer(lambda: multiply3DmatricesPython(catImg, catImg), setup=setupPython).timeit(number=numOfExecutions)
cythonTimeMatrixMul = timeit.Timer(lambda: mwe.multiply3DmatricesCython(catImg, catImg), setup=setupCython).timeit(number=numOfExecutions)
pybind11TimeMatrixMul_using_stdvector = timeit.Timer(lambda: module_name.multiply_3d_arrays_using_stdvector(catImg, catImg), setup=setupPybind11).timeit(number=numOfExecutions)
# pybind11TimeMatrixMul_using_eigenlibs = timeit.Timer(lambda: module_name.multiply_3d_arrays_using_eigenlibs(np.array([catImg[:,:,0], catImg[:,:,1], catImg[:,:,2]]), np.array([catImg[:,:,0], catImg[:,:,1], catImg[:,:,2]])), setup=setupPybind11).timeit(number=numOfExecutions)
pybind11TimeMatrixMul_using_eigenlibs = timeit.Timer(lambda: module_name.multiply_3d_arrays_using_eigenlibs(np.transpose(catImg, (2, 0, 1)), np.transpose(catImg, (2, 0, 1))), setup=setupPybind11).timeit(number=numOfExecutions)

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

mat_python = multiply3DmatricesPython(catImg, catImg)
mat_numpy = multiply3DmatricesNumpy(catImg, catImg)
mat_eiglibs = module_name.multiply_3d_arrays_using_eigenlibs(np.array([catImg[:,:,0], catImg[:,:,1], catImg[:,:,2]]), np.array([catImg[:,:,0], catImg[:,:,1], catImg[:,:,2]]))
# mat_eiglibs = np.asfortranarray(module_name.multiply_3d_arrays_using_eigenlibs(catImg, catImg))
print("mat_eiglibs order row major? =" + str(mat_eiglibs.flags['C_CONTIGUOUS']))
# mat_eiglibs = np.ascontiguousarray(mat_eiglibs)

print("mat_python=" + str(mat_python))
print("mat_python_1=" + str(mat_python[:,:,0]))
print("mat_python_2=" + str(mat_python[:,:,1]))
print("mat_python_3=" + str(mat_python[:,:,2]))
print("")
print("mat_numpy=" + str(mat_numpy))
print("mat_numpy_1=" + str(mat_numpy[:,:,0]))
print("mat_numpy_2=" + str(mat_numpy[:,:,1]))
print("mat_numpy_3=" + str(mat_numpy[:,:,2]))
print("")
print("mat_eiglibs=" + str(mat_eiglibs))
print("mat_eiglibs_1=" + str(mat_eiglibs[0,:,:]))
print("mat_eiglibs_2=" + str(mat_eiglibs[1,:,:]))
print("mat_eiglibs_3=" + str(mat_eiglibs[2,:,:]))
print("mat_eiglibs_1_zeile1_spalte2=" + str(mat_eiglibs[0,0,1]))
print("mat_eiglibs_transpose=" + str(np.transpose(mat_eiglibs, (1, 2, 0))))

def show_image(img_array):
    # Convert the NumPy array to uint8
    img_array = np.uint8(img_array)

    # Show the image
    cv2.imshow('Resulting Image', img_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("mat_numpy.shape=" + str(mat_numpy.shape))
print("mat_eiglibs.shape=" + str(mat_eiglibs.shape))

show_image(catImg)
show_image(mat_python)
show_image(mat_numpy)
show_image(np.transpose(mat_eiglibs, (1, 2, 0)))

# print(np.array_equal(mat_numpy, mat_numpy))
# print(np.array_equal(mat_numpy, mat_python))
# print(np.array_equal(mat_numpy, mat_eiglibs))

# arr1 = np.array([[[1, 5, 9], [2, 6, 10]], [[3, 7, 11], [4, 8, 12]]])
# arr1 = np.asfortranarray(arr1)
# print(arr1)
# print("arr1_0=" + str(arr1[:,:,0]))
# print("arr1_1=" + str(arr1[:,:,1]))
# print("arr1_2=" + str(arr1[:,:,2]))
# print(arr1.shape)

# module_name.test_ordering(arr1)



# # Define the 2x2x3 numpy array
# arr = np.array([[[1, 5, 9], [2, 6, 10]], [[3, 7, 11], [4, 8, 12]]])
# arr2 = arr.reshape(3,2,2, order="C")
# arr3 = arr.reshape(3,2,2, order="F")
# arr4 = arr.reshape(2,3,2, order="C")
# arr5 = arr.reshape(2,3,2, order="F")
# print("arr_0=" + str(arr[:,:,0]))
# print("arr_1=" + str(arr[:,:,1]))
# print("arr_2=" + str(arr[:,:,2]))
# print(arr)
# print(arr2)
# print(arr3)
# print(arr4)
# print(arr5)

# # Ensure the array is C_CONTIGUOUS
# arr = np.ascontiguousarray(arr)
# module_name.test_ordering2(arr, arr)