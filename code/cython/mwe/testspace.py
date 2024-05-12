import timeit
import numpy as np
# import pyximport; pyximport.install(pyimport=True)
import master as mwe
# import npTest
# import basicArithmetic
# import Multiply_wrapper
# import npTest


add_result = mwe.add(2,3)
print(str(add_result) + str(type(add_result)))

## speed comparison between pure python loops and with typeinformation using cython
pythonTime = timeit.timeit('master.sum_of_first_n_numbers_py(1000)', setup='import master', number=100)
cythonTime = timeit.timeit('master.sum_of_first_n_numbers_cy(1000)', setup='import master', number=100)

print("pythonTime=" + str(pythonTime))
print("cythonTime=" + str(cythonTime))
print("Cython is {}x faster".format(pythonTime/cythonTime))

## C++ class API test
multiply_obj = mwe.PyMultiply(1.5, 3)
multiply_obj = mwe.PyMultiply(1.5, 3)
print(multiply_obj.multiply())
print(dir(multiply_obj))

## Testing numpy interface
newArray = mwe.add_numpy_elements(np.array([[1, 2, 3]]))
print(str(newArray) + ", type=" + str(type(newArray)))