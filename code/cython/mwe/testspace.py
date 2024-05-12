import timeit
import numpy as np
# import pyximport; pyximport.install(pyimport=True)
# import mwe
# import Multiply_wrapper
import npTest


# add_result = mwe.add(2,3)
# print(str(add_result) + str(type(add_result)))

# sub_result = mwe.sub(2,3)
# print(str(sub_result) + str(type(sub_result)))

# mul_result = mwe.mul(2,3)
# print(str(mul_result) + str(type(mul_result)))

# div_result = mwe.div(2,3)
# print(str(div_result) + str(type(div_result)))


# # speed comparison between pure python loops and with typeinformation using cython
# pythonTime = timeit.timeit('cyMath.sum_of_first_n_numbers_py(1000)', setup='import mwe', number=100)
# cythonTime = timeit.timeit('cyMath.sum_of_first_n_numbers_cy(1000)', setup='import mwe', number=100)

# print("pythonTime=" + str(pythonTime))
# print("cythonTime=" + str(cythonTime))
# print("Cython is {}x faster".format(pythonTime/cythonTime))

# # C++ class API test
# multiply_obj = Multiply_wrapper.PyMultiply(1.5, 3)
# print(multiply_obj.multiply())
# print(dir(multiply_obj))

# Testing numpy interface
newArray = npTest.add_numpy_elements(np.array([[1, 2, 3]]))
print(str(newArray) + ", type=" + str(type(newArray)))