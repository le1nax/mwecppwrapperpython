import numpy as np
import master as mwe

# Create a sample 3D array
arr1 = np.random.randint(0, 100, size=(3, 2, 2), dtype=np.uint64)

# Call the Cython function
result = mwe.multiply3DmatricesCythonUsingEigen(arr1)

print(result)
